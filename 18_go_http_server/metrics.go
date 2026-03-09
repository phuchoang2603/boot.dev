package main

import (
	"fmt"
	"net/http"
)

func (c *apiConfig) middlewareMetricsInc(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, req *http.Request) {
		c.fileserverHits.Add(1)
		next.ServeHTTP(w, req)
	})
}

func (c *apiConfig) handlerMetrics(w http.ResponseWriter, req *http.Request) {
	w.Header().Add("Content-Type", "text/html")
	w.WriteHeader(http.StatusOK)

	fmt.Fprintf(w,
		"<html> <body> <h1>Welcome, Chirpy Admin</h1> <p>Chirpy has been visited %d times!</p> </body> </html>",
		c.fileserverHits.Load())
}

func (c *apiConfig) handlerReset(w http.ResponseWriter, req *http.Request) {
	w.Header().Add("Content-Type", "text/plain; charset=utf-8")
	w.WriteHeader(http.StatusOK)

	c.fileserverHits.Store(0)
	fmt.Fprintf(w, "Reset hit to 0")
}
