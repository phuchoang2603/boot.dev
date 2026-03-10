package main

import (
	"encoding/json"
	"net/http"
	"slices"
	"strings"
	"time"

	"github.com/google/uuid"
	"github.com/phuchoang2603/boot.dev/18_go_http_server/internal/database"
)

type Chirp struct {
	ID        uuid.UUID `json:"id"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	Body      string    `json:"body"`
	UserID    uuid.UUID `json:"user_id"`
}

func (c *apiConfig) handlerCreateChirp(w http.ResponseWriter, req *http.Request) {
	params := struct {
		Body   string    `json:"body"`
		UserID uuid.UUID `json:"user_id"`
	}{}

	resp := Chirp{}

	decoder := json.NewDecoder(req.Body)
	if err := decoder.Decode(&params); err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error decoding request body", err)
		return
	}

	if len(params.Body) > 140 {
		respondWithError(w, http.StatusBadRequest, "Chirp is too long", nil)
		return
	}

	chirp, err := c.db.CreateChirps(req.Context(), database.CreateChirpsParams{
		Body:   replaceBadWord(params.Body),
		UserID: params.UserID,
	})
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error creating chirp", err)
	}

	resp.ID = chirp.ID
	resp.CreatedAt = chirp.CreatedAt
	resp.UpdatedAt = chirp.UpdatedAt
	resp.Body = chirp.Body
	resp.UserID = chirp.UserID

	respondWithJSON(w, http.StatusCreated, resp)
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

func (c *apiConfig) handlerGetChirps(w http.ResponseWriter, req *http.Request) {
	chirps, err := c.db.GetChirps(req.Context())
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error getting chirps", err)
		return
	}

	resp := []Chirp{}

	for _, chirp := range chirps {
		resp = append(resp, Chirp{
			ID:        chirp.ID,
			CreatedAt: chirp.CreatedAt,
			UpdatedAt: chirp.UpdatedAt,
			Body:      chirp.Body,
			UserID:    chirp.UserID,
		})
	}

	respondWithJSON(w, http.StatusOK, resp)
}

func (c *apiConfig) handlerGetChirpByID(w http.ResponseWriter, req *http.Request) {
	id, err := uuid.Parse(req.PathValue("chirpID"))
	if err != nil {
		respondWithError(w, http.StatusBadRequest, "Invalid chirp ID", err)
		return
	}

	chirp, err := c.db.GetChirpById(req.Context(), id)
	if err != nil {
		respondWithError(w, http.StatusNotFound, "Error getting chirp", err)
		return
	}

	resp := Chirp{
		ID:        chirp.ID,
		CreatedAt: chirp.CreatedAt,
		UpdatedAt: chirp.UpdatedAt,
		Body:      chirp.Body,
		UserID:    chirp.UserID,
	}

	respondWithJSON(w, http.StatusOK, resp)
}
