package main

import (
	"encoding/json"
	"net/http"
	"slices"
	"strings"
)

func handlerChirpsValidate(w http.ResponseWriter, req *http.Request) {
	params := struct {
		Body string `json:"body"`
	}{}

	resp := struct {
		CleanedBody string `json:"cleaned_body"`
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

	resp.CleanedBody = replaceBadWord(params.Body)
	respondWithJSON(w, 200, resp)
}

func replaceBadWord(body string) (cleanedBody string) {
	badWords := []string{
		"kerfuffle",
		"sharbert",
		"fornax",
	}

	cleanedWords := []string{}

	for word := range strings.SplitSeq(body, " ") {
		if slices.Contains(badWords, strings.ToLower(word)) {
			cleanedWords = append(cleanedWords, "****")
		} else {
			cleanedWords = append(cleanedWords, word)
		}
	}

	return strings.Join(cleanedWords, " ")
}
