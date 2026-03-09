package main

import (
	"encoding/json"
	"net/http"
	"time"

	"github.com/google/uuid"
)

type User struct {
	ID        uuid.UUID `json:"id"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
	Email     string    `json:"email"`
}

func (c *apiConfig) handlerCreateUser(w http.ResponseWriter, req *http.Request) {
	params := struct {
		Email string `json:"email"`
	}{}

	resp := User{}

	decoder := json.NewDecoder(req.Body)
	if err := decoder.Decode(&params); err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error decoding request body", err)
		return
	}

	user, err := c.db.CreateUser(req.Context(), params.Email)
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error creating user", err)
	}

	resp.ID = user.ID
	resp.CreatedAt = user.CreatedAt
	resp.UpdatedAt = user.UpdatedAt
	resp.Email = user.Email

	respondWithJSON(w, http.StatusCreated, resp)
}
