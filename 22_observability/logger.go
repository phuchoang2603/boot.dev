package main

import (
	"errors"
	"fmt"
	"log/slog"
	"net/url"
	"os"
	"slices"

	"boot.dev/linko/internal/linkoerr"
	"github.com/lmittmann/tint"
	"github.com/mattn/go-isatty"
	"github.com/natefinch/lumberjack"
	pkgerr "github.com/pkg/errors"
)

var sensitiveKeys = []string{"password", "key", "apikey", "secret", "pin", "creditcardno", "user"}

type closeFunc func() error

type stackTracer interface {
	error
	StackTrace() pkgerr.StackTrace
}

type multiError interface {
	error
	Unwrap() []error
}

func initializeLogger(logFile string) (*slog.Logger, closeFunc, error) {
	handlers := []slog.Handler{
		tint.NewHandler(os.Stderr, &tint.Options{
			NoColor:     !isatty.IsCygwinTerminal(os.Stdout.Fd()) && !isatty.IsTerminal(os.Stdout.Fd()),
			Level:       slog.LevelDebug,
			ReplaceAttr: replaceAttr,
		}),
	}
	closers := []closeFunc{}

	if logFile != "" {
		rotationLogger := &lumberjack.Logger{
			Filename:   logFile,
			MaxSize:    1,
			MaxAge:     28,
			MaxBackups: 10,
			LocalTime:  false,
			Compress:   true,
		}

		handlers = append(handlers,
			slog.NewJSONHandler(rotationLogger, &slog.HandlerOptions{
				Level:       slog.LevelInfo,
				ReplaceAttr: replaceAttr,
			}),
		)

		closers = append(closers, func() error {
			if err := rotationLogger.Close(); err != nil {
				return err
			}
			return nil
		},
		)
	}

	closer := func() error {
		var errs []error
		for _, close := range closers {
			if err := close(); err != nil {
				errs = append(errs, err)
			}
		}
		return errors.Join(errs...)
	}

	return slog.New(slog.NewMultiHandler(handlers...)), closer, nil
}

func errorAttrs(err error) []slog.Attr {
	attrs := []slog.Attr{
		slog.String("message", err.Error()),
	}

	attrs = append(attrs, linkoerr.Attrs(err)...)

	if stackErr, ok := errors.AsType[stackTracer](err); ok {
		attrs = append(attrs, slog.String("stack_trace", fmt.Sprintf("%+v", stackErr.StackTrace())))
	}

	return attrs
}

func replaceAttr(groups []string, a slog.Attr) slog.Attr {
	if a.Key == "error" {
		switch e := a.Value.Any().(type) {
		case multiError:
			var errAttrs []slog.Attr
			for i, err := range e.Unwrap() {
				errAttrs = append(
					errAttrs,
					slog.GroupAttrs(fmt.Sprintf("error_%d", i+1), errorAttrs(err)...),
				)
			}
			return slog.GroupAttrs("errors", errAttrs...)
		case error:
			return slog.GroupAttrs("error", errorAttrs(e)...)
		default:
			return a
		}
	}

	if slices.Contains(sensitiveKeys, a.Key) {
		return slog.String(a.Key, "[REDACTED]")
	}

	if u, err := url.Parse(a.Value.String()); err == nil {
		if _, hasPassword := u.User.Password(); hasPassword {
			u.User = url.UserPassword(u.User.Username(), "[REDACTED]")
			return slog.String(a.Key, u.String())
		}
	}

	return a
}
