package main

import (
	"bufio"
	"errors"
	"fmt"
	"log/slog"
	"os"

	pkgerr "github.com/pkg/errors"
)

type closeFunc func() error

type stackTracer interface {
	error
	StackTrace() pkgerr.StackTrace
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

func replaceAttr(groups []string, a slog.Attr) slog.Attr {
	if a.Key == "error" {
		err, ok := a.Value.Any().(error)
		if !ok {
			return a
		}
		if stackErr, ok := errors.AsType[stackTracer](err); ok {
			return slog.GroupAttrs("error",
				slog.Attr{Key: "message", Value: slog.StringValue(stackErr.Error())},
				slog.Attr{Key: "stack_trace", Value: slog.StringValue(fmt.Sprintf("%+v", stackErr.StackTrace()))})
		}
	}
	return a
}
