package main

import (
	"bufio"
	"errors"
	"fmt"
	"log/slog"
	"os"

	"boot.dev/linko/internal/linkoerr"
	pkgerr "github.com/pkg/errors"
)

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
		slog.NewTextHandler(os.Stderr, &slog.HandlerOptions{
			Level:       slog.LevelDebug,
			ReplaceAttr: replaceAttr,
		}),
	}
	closers := []closeFunc{}

	if logFile != "" {
		file, err := os.OpenFile(logFile, os.O_WRONLY|os.O_CREATE|os.O_APPEND, 0o644)
		if err != nil {
			return nil, func() error { return nil }, fmt.Errorf("failed to open log file: %w", err)
		}
		bufferedFile := bufio.NewWriterSize(file, 8192)

		handlers = append(handlers,
			slog.NewJSONHandler(bufferedFile, &slog.HandlerOptions{
				Level:       slog.LevelInfo,
				ReplaceAttr: replaceAttr,
			}),
		)

		closers = append(closers, func() error {
			if err := bufferedFile.Flush(); err != nil {
				return err
			}
			if err = file.Close(); err != nil {
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
	return a
}
