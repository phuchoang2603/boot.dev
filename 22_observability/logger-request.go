package main

import (
	"context"
	"fmt"
	"io"
	"net"
	"net/http"
)

type spyReadCloser struct {
	io.ReadCloser
	bytesRead int
}

func (r *spyReadCloser) Read(p []byte) (int, error) {
	n, err := r.ReadCloser.Read(p)
	r.bytesRead += n
	return n, err
}

type spyResponseWriter struct {
	http.ResponseWriter
	bytesWritten int
	statusCode   int
}

func (w *spyResponseWriter) Write(p []byte) (int, error) {
	if w.statusCode == 0 {
		w.statusCode = http.StatusOK
	}
	n, err := w.ResponseWriter.Write(p)
	w.bytesWritten += n
	return n, err
}

func (w *spyResponseWriter) WriteHeader(statusCode int) {
	w.statusCode = statusCode
	w.ResponseWriter.WriteHeader(statusCode)
}

const logContextKey contextKey = "log_context"

type LogContext struct {
	Username string
	Error    error
}

func httpError(ctx context.Context, w http.ResponseWriter, err error, status int) {
	if logCtx, ok := ctx.Value(logContextKey).(*LogContext); ok {
		logCtx.Error = err
	}

	msg := err.Error()
	switch status {
	case http.StatusUnauthorized, http.StatusForbidden, http.StatusInternalServerError:
		msg = http.StatusText(status)
	}

	http.Error(w, msg, status)
}

func redactIP(hostport string) string {
	host, _, err := net.SplitHostPort(hostport)
	if err != nil {
		return hostport
	}

	ip := net.ParseIP(host)
	if ip == nil {
		return host
	}

	if ip.Equal(net.IPv6loopback) {
		ip = net.IPv4(127, 0, 0, 1)
	}

	ip4 := ip.To4()
	if ip4 == nil {
		return host
	}

	return fmt.Sprintf("%d.%d.%d.x", ip4[0], ip4[1], ip4[2])
}
