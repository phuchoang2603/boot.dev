package main

import (
	"encoding/json"
	"net/http"
	"time"

	"github.com/google/uuid"
	"github.com/phuchoang2603/boot.dev/18_go_http_server/internal/auth"
	"github.com/phuchoang2603/boot.dev/18_go_http_server/internal/database"
)

const jwtExpiration = 3600 * time.Second

type User struct {
	ID          uuid.UUID `json:"id"`
	CreatedAt   time.Time `json:"created_at"`
	UpdatedAt   time.Time `json:"updated_at"`
	Email       string    `json:"email"`
	IsChirpyRed bool      `json:"is_chirpy_red"`
}

func (c *apiConfig) handlerCreateUser(w http.ResponseWriter, req *http.Request) {
	params := struct {
		Password string `json:"password"`
		Email    string `json:"email"`
	}{}

	decoder := json.NewDecoder(req.Body)
	if err := decoder.Decode(&params); err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error decoding request body", err)
		return
	}

	hashedPassword, err := auth.HashPassword(params.Password)
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error hashing password", err)
		return
	}

	user, err := c.db.CreateUser(req.Context(), database.CreateUserParams{
		Email:          params.Email,
		HashedPassword: hashedPassword,
	})
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error creating user", err)
	}

	resp := User{
		ID:          user.ID,
		CreatedAt:   user.CreatedAt,
		UpdatedAt:   user.UpdatedAt,
		Email:       user.Email,
		IsChirpyRed: user.IsChirpyRed,
	}

	respondWithJSON(w, http.StatusCreated, resp)
}

func (c *apiConfig) handlerUpdateUser(w http.ResponseWriter, req *http.Request) {
	accessToken, err := auth.GetBearerToken(req.Header)
	if err != nil {
		respondWithError(w, http.StatusUnauthorized, "Unauthorized", err)
		return
	}

	validUserID, err := auth.ValidateJWT(accessToken, c.jwtSecret)
	if err != nil {
		respondWithError(w, http.StatusUnauthorized, "Unauthorized", err)
		return
	}

	params := struct {
		Password string `json:"password"`
		Email    string `json:"email"`
	}{}

	decoder := json.NewDecoder(req.Body)
	if err := decoder.Decode(&params); err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error decoding request body", err)
		return
	}

	hashedPassword, err := auth.HashPassword(params.Password)
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error hashing password", err)
		return
	}

	user, err := c.db.UpdateUser(req.Context(), database.UpdateUserParams{
		ID:             validUserID,
		Email:          params.Email,
		HashedPassword: hashedPassword,
	})
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error updating user", err)
		return
	}

	resp := User{
		ID:          user.ID,
		CreatedAt:   user.CreatedAt,
		UpdatedAt:   user.UpdatedAt,
		Email:       user.Email,
		IsChirpyRed: user.IsChirpyRed,
	}

	respondWithJSON(w, http.StatusOK, resp)
}

func (c *apiConfig) handlerLoginUser(w http.ResponseWriter, req *http.Request) {
	params := struct {
		Password string `json:"password"`
		Email    string `json:"email"`
	}{}

	decoder := json.NewDecoder(req.Body)
	if err := decoder.Decode(&params); err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error decoding request body", err)
		return
	}

	user, err := c.db.GetUserByEmail(req.Context(), params.Email)
	if err != nil {
		respondWithError(w, http.StatusUnauthorized, "User not found", nil)
		return
	}

	isValid, err := auth.CheckPasswordHash(params.Password, user.HashedPassword)
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error checking password hash", err)
		return
	}

	if !isValid {
		respondWithError(w, http.StatusUnauthorized, "Incorrect email or password", nil)
		return
	}

	accessToken, err := auth.MakeJWT(user.ID, c.jwtSecret, jwtExpiration)
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error generating JWT", err)
		return
	}

	refreshToken, err := c.db.CreateRefreshToken(req.Context(), database.CreateRefreshTokenParams{
		Token:  auth.MakeRefreshToken(),
		UserID: user.ID,
	})
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error creating refresh token", err)
		return
	}

	resp := struct {
		User
		Token        string `json:"token"`
		RefreshToken string `json:"refresh_token"`
	}{
		User: User{
			ID:          user.ID,
			CreatedAt:   user.CreatedAt,
			UpdatedAt:   user.UpdatedAt,
			Email:       user.Email,
			IsChirpyRed: user.IsChirpyRed,
		},
		Token:        accessToken,
		RefreshToken: refreshToken.Token,
	}

	respondWithJSON(w, http.StatusOK, resp)
}

func (c *apiConfig) handlerRefreshToken(w http.ResponseWriter, req *http.Request) {
	refreshToken, err := auth.GetBearerToken(req.Header)
	if err != nil {
		respondWithError(w, http.StatusUnauthorized, "Couldn't find token", err)
		return
	}

	user, err := c.db.GetUserFromRefreshToken(req.Context(), refreshToken)
	if err != nil {
		respondWithError(w, http.StatusUnauthorized, "Error getting user from refresh token", err)
		return
	}

	token, err := auth.MakeJWT(user.ID, c.jwtSecret, jwtExpiration)
	if err != nil {
		respondWithError(w, http.StatusInternalServerError, "Couldn't validate token", err)
		return
	}

	respondWithJSON(w, http.StatusOK, map[string]string{
		"token": token,
	})
}

func (c *apiConfig) handlerRevokeToken(w http.ResponseWriter, req *http.Request) {
	refreshToken, err := auth.GetBearerToken(req.Header)
	if err != nil {
		respondWithError(w, http.StatusUnauthorized, "Unauthorized", err)
		return
	}

	if err := c.db.RevokeRefreshToken(req.Context(), refreshToken); err != nil {
		respondWithError(w, http.StatusInternalServerError, "Error revoke token", err)
	}

	w.WriteHeader(http.StatusNoContent)
}
