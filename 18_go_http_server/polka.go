package main

import (
	"encoding/json"
	"net/http"

	"github.com/google/uuid"
	"github.com/phuchoang2603/boot.dev/18_go_http_server/internal/auth"
	"github.com/phuchoang2603/boot.dev/18_go_http_server/internal/database"
)

func (c *apiConfig) handlerUpgradeChirpyRead(w http.ResponseWriter, req *http.Request) {
	apiKey, err := auth.GetAPIKey(req.Header)
	if err != nil {
		respondWithError(w, http.StatusUnauthorized, "Unauthorized", err)
		return
	}

	if apiKey != c.polkaKey {
		respondWithError(w, http.StatusUnauthorized, "Unauthorized", nil)
		return
	}

	params := struct {
		Event string `json:"event"`
		Data  struct {
			UserID uuid.UUID `json:"user_id"`
		} `json:"data"`
	}{}

	decoder := json.NewDecoder(req.Body)
	if err := decoder.Decode(&params); err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error decoding request body", err)
		return
	}

	if params.Event != "user.upgraded" {
		w.WriteHeader(http.StatusNoContent)
		return
	}

	if _, err := c.db.UpdateChirpyRed(req.Context(), database.UpdateChirpyRedParams{
		ID:          params.Data.UserID,
		IsChirpyRed: true,
	}); err != nil {
		respondWithError(w, http.StatusUnauthorized, "Unauthorized", err)
	}

	w.WriteHeader(http.StatusNoContent)
}
