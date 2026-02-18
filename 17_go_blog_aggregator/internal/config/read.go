package config

import (
	"encoding/json"
	"os"
	"path/filepath"
)

func getConfigFilePath() (string, error) {
	home, err := os.UserHomeDir()
	if err != nil {
		return "", err
	} else {
		return filepath.Join(home, configFileName), nil
	}
}

func Read() (cfg Config, err error) {
	configFilePath, err := getConfigFilePath()
	if err != nil {
		return Config{}, err
	}

	file, err := os.Open(configFilePath)
	if err != nil {
		return Config{}, err
	}
	defer file.Close()

	decoder := json.NewDecoder(file)
	if err := decoder.Decode(&cfg); err != nil {
		return Config{}, err
	}

	return cfg, nil
}

func write(cfg Config) error {
	configFilePath, err := getConfigFilePath()
	if err != nil {
		return err
	}

	file, err := os.Create(configFilePath)
	if err != nil {
		return err
	}
	defer file.Close()

	encoder := json.NewEncoder(file)
	if err := encoder.Encode(cfg); err != nil {
		return err
	}

	return nil
}
