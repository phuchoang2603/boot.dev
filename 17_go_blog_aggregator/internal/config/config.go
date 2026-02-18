// Package config provides configuration management for the Go Blog Aggregator application.
package config

const configFileName = ".gatorconfig.json"

type Config struct {
	DBURL           string `json:"db_url"`
	CurrentUserName string `json:"current_user_name"`
}

func (cfg *Config) SetUser(user string) error {
	cfg.CurrentUserName = user
	if err := write(*cfg); err != nil {
		return err
	}
	return nil
}
