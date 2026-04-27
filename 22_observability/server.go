package main

import (
	"context"
	"errors"
	"fmt"
	"log/slog"
	"net"
	"net/http"
	nethttppprof "net/http/pprof"
	"os"

	"boot.dev/linko/internal/store"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"
)

type server struct {
	httpServer *http.Server
	store      store.Store
	cancel     context.CancelFunc
	logger     *slog.Logger
}

func newServer(store store.Store, port int, cancel context.CancelFunc, logger *slog.Logger) *server {
	mux := http.NewServeMux()

	srv := &http.Server{
		Addr:    fmt.Sprintf(":%d", port),
		Handler: otelhttp.NewHandler(metricsMiddleware(requestTracing(requestLogger(logger)(mux))), "http.server"),
	}

	s := &server{
		httpServer: srv,
		store:      store,
		cancel:     cancel,
		logger:     logger,
	}

	mux.Handle(
		"POST /api/login",
		withSpan("handler.login", s.authMiddleware(http.HandlerFunc(s.handlerLogin))),
	)
	mux.Handle(
		"POST /api/shorten",
		withSpan("handler.shorten_link", s.authMiddleware(http.HandlerFunc(s.handlerShortenLink))),
	)
	mux.Handle(
		"GET /api/stats",
		withSpan("handler.stats", s.authMiddleware(http.HandlerFunc(s.handlerStats))),
	)
	mux.Handle(
		"GET /api/urls",
		withSpan("handler.list_urls", s.authMiddleware(http.HandlerFunc(s.handlerListURLs))),
	)
	mux.Handle("GET /", withSpan("handler.index", http.HandlerFunc(s.handlerIndex)))
	mux.Handle("GET /{shortCode}", withSpan("handler.redirect", http.HandlerFunc(s.handlerRedirect)))
	mux.Handle("POST /admin/shutdown", withSpan("handler.shutdown", http.HandlerFunc(s.handlerShutdown)))

	mux.Handle("GET /metrics", promhttp.Handler())
	mux.Handle("GET /debug/pprof", s.authMiddleware(http.HandlerFunc(nethttppprof.Index)))
	mux.Handle("GET /debug/pprof/profile", s.authMiddleware(http.HandlerFunc(nethttppprof.Profile)))

	return s
}

func (s *server) start() error {
	ln, err := net.Listen("tcp", s.httpServer.Addr)
	if err != nil {
		return err
	}
	s.logger.Debug(fmt.Sprintf("Linko is running on http://localhost:%d", ln.Addr().(*net.TCPAddr).Port))
	if err := s.httpServer.Serve(ln); !errors.Is(err, http.ErrServerClosed) {
		return err
	}
	return nil
}

func (s *server) shutdown(ctx context.Context) error {
	return s.httpServer.Shutdown(ctx)
}

func (s *server) handlerShutdown(w http.ResponseWriter, r *http.Request) {
	if os.Getenv("ENV") == "production" {
		http.NotFound(w, r)
		return
	}
	w.WriteHeader(http.StatusOK)
	go s.cancel()
}
