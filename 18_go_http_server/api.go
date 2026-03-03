package main

import (
	"encoding/json"
	"log"
	"net/http"
)

func validateChirp(w http.ResponseWriter, req *http.Request) {
	params := struct {
		Body string `json:"body"`
	}{}

	resp := struct {
		Valid bool `json:"valid"`
	}{}

	decoder := json.NewDecoder(req.Body)
	if err := decoder.Decode(&params); err != nil {
		respondWithError(w, 500, "Error decoding request body")
		return
	}

	if len(params.Body) > 140 {
		respondWithError(w, 400, "Chirp is too long")
		return
	}

	resp.Valid = true
	respondWithJSON(w, 200, resp)
}

func respondWithError(w http.ResponseWriter, code int, msg string) {
	respBody := struct {
		Error string `json:"error"`
	}{
		Error: msg,
	}

	data, err := json.Marshal(respBody)
	if err != nil {
		log.Printf("Error marshaling response body: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(code)
	w.Write(data)
}

func respondWithJSON(w http.ResponseWriter, code int, payload any) {
	data, err := json.Marshal(payload)
	if err != nil {
		log.Printf("Error marshaling response body: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(code)
	w.Write(data)
}
