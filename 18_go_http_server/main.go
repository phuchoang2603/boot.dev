package main

import (
	"log"
	"net/http"
	"sync/atomic"
)

func main() {
	const port = "8080"
	const filePath = "."
	mux := http.NewServeMux()
	cfg := apiConfig{
		fileserverHits: atomic.Int32{},
	}

	fileServerHandler := http.StripPrefix("/app", http.FileServer(http.Dir(filePath)))
	mux.Handle("/app/", cfg.middlewareMetricsInc(fileServerHandler))
	mux.HandleFunc("POST /api/validate_chirp", validateChirp)

	mux.HandleFunc("GET /api/healthz", serveReadiness)
	mux.HandleFunc("GET /admin/metrics", cfg.getMetrics)
	mux.HandleFunc("POST /admin/reset", cfg.resetMetrics)

	srv := &http.Server{
		Addr:    ":" + port,
		Handler: mux,
	}

	log.Printf("Serving files from %s on port: %s\n", filePath, port)
	log.Fatal(srv.ListenAndServe())
}
