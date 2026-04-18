package linkoerr

import (
	"errors"
	"log/slog"
)

type errWithAttrs struct {
	error
	attrs []slog.Attr
}

type attrError interface {
	Attrs() []slog.Attr
}

func WithAttrs(err error, args ...any) error {
	return &errWithAttrs{
		error: err,
		attrs: argsToAttr(args),
	}
}

func (e *errWithAttrs) Unwrap() error {
	return e.error
}

func (e *errWithAttrs) Attrs() []slog.Attr {
	return e.attrs
}

// Attrs recursively extracts all logging attributes from an error chain. In the
// case of duplicate keys, the outermost value takes precedence.
func Attrs(err error) []slog.Attr {
	var attrs []slog.Attr
	for err != nil {
		if ae, ok := err.(attrError); ok {
			attrs = append(attrs, ae.Attrs()...)
		}
		err = errors.Unwrap(err)
	}
	return attrs
}
