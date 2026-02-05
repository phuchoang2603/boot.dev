package pokecache_test

import (
	"testing"
	"time"

	"github.com/phuchoang2603/boot.dev/15_go_pokedex_cli/internal/pokecache"
)

func TestCache_ReapLoop(t *testing.T) {
	tests := []struct {
		name      string
		cinterval time.Duration // The cache's reap interval
		waitTime  time.Duration // How long to wait for the first check (should be < cinterval)
	}{
		{
			name:      "reap expired entries",
			cinterval: 20 * time.Millisecond,
			waitTime:  30 * time.Millisecond, // Enough time for the ticker to fire
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			c := pokecache.NewCache(tt.cinterval)

			key := "test-key"
			c.Add(key, []byte("value"))

			// 1. IMMEDIATE CHECK: Should still be there
			if _, found := c.Get(key); !found {
				t.Errorf("expected key %q to exist immediately after adding", key)
			}

			// 2. MID-INTERVAL CHECK: Should still be there
			time.Sleep(tt.cinterval / 2)
			if _, found := c.Get(key); !found {
				t.Errorf("expected key %q to still exist before interval reached", key)
			}

			// 3. POST-INTERVAL CHECK: Should be reaped
			time.Sleep(tt.waitTime)
			if _, found := c.Get(key); found {
				t.Errorf("expected key %q to be reaped after %v", key, tt.waitTime)
			}
		})
	}
}

func TestCache_Add(t *testing.T) {
	tests := []struct {
		name string // description of this test case
		// Named input parameters for receiver constructor.
		interval time.Duration
		// Named input parameters for target function.
		key string
		val []byte
	}{
		{
			name:     "add new entry",
			interval: time.Minute,
			key:      "pokemon1",
			val:      []byte("pikachu"),
		},
		{
			name:     "overwrite existing entry",
			interval: time.Minute,
			key:      "pokemon1",
			val:      []byte("charizard"),
		},
		{
			name:     "add empty value",
			interval: time.Minute,
			key:      "empty",
			val:      []byte{},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			c := pokecache.NewCache(tt.interval)
			c.Add(tt.key, tt.val)

			// Verify the entry was added
			got, found := c.Get(tt.key)
			if !found {
				t.Errorf("Add() failed to add entry")
			}
			if string(got) != string(tt.val) {
				t.Errorf("Add() = %v, want %v", got, tt.val)
			}
		})
	}
}

func TestCache_Get(t *testing.T) {
	tests := []struct {
		name string // description of this test case
		// Named input parameters for receiver constructor.
		interval time.Duration
		// Named input parameters for target function.
		key   string
		want  []byte
		want2 bool
	}{
		{
			name:     "get existing entry",
			interval: time.Minute,
			key:      "pokemon1",
			want:     []byte("bulbasaur"),
			want2:    true,
		},
		{
			name:     "get non-existent entry",
			interval: time.Minute,
			key:      "nonexistent",
			want:     nil,
			want2:    false,
		},
		{
			name:     "get empty entry",
			interval: time.Minute,
			key:      "empty",
			want:     []byte{},
			want2:    true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			c := pokecache.NewCache(tt.interval)

			// Add test entries that should exist
			if tt.want2 {
				c.Add("pokemon1", []byte("bulbasaur"))
				c.Add("empty", []byte{})
			}

			got, got2 := c.Get(tt.key)

			if !tt.want2 && got2 {
				t.Errorf("Get() found = %v, want %v", got2, tt.want2)
			}
			if tt.want2 && !got2 {
				t.Errorf("Get() found = %v, want %v", got2, tt.want2)
			}
			if tt.want2 && string(got) != string(tt.want) {
				t.Errorf("Get() value = %v, want %v", got, tt.want)
			}
		})
	}
}
