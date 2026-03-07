package main

import (
	"encoding/json"
	"net/http"
)

func handlerChirpsValidate(w http.ResponseWriter, req *http.Request) {
	params := struct {
		Body string `json:"body"`
	}{}

	resp := struct {
		Valid bool `json:"valid"`
	}{}

	decoder := json.NewDecoder(req.Body)
	if err := decoder.Decode(&params); err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error decoding request body", err)
		return
	}

	if len(params.Body) > 140 {
		respondWithError(w, http.StatusBadRequest, "Chirp is too long", nil)
		return
	}

	resp.Valid = true
	respondWithJSON(w, 200, resp)
}
