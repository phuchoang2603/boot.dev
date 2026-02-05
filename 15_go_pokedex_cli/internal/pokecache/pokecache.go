// Package pokecache provides caching for interacting with the Pokémon API faster.
package pokecache

import (
	"sync"
	"time"
)

type Cache struct {
	mu      *sync.RWMutex
	entries map[string]cacheEntry
}

type cacheEntry struct {
	createdAt time.Time
	val       []byte
}

func NewCache(interval time.Duration) Cache {
	cache := Cache{
		&sync.RWMutex{},
		make(map[string]cacheEntry),
	}
	go cache.ReapLoop(interval)
	return cache
}

func (c *Cache) Add(key string, val []byte) {
	c.mu.Lock()
	defer c.mu.Unlock()

	c.entries[key] = cacheEntry{
		time.Now().UTC(),
		val,
	}
}

func (c *Cache) Get(key string) ([]byte, bool) {
	c.mu.RLock()
	defer c.mu.RUnlock()

	cache, found := c.entries[key]
	return cache.val, found
}

func (c *Cache) ReapLoop(interval time.Duration) {
	reapTicker := time.Tick(interval)

	for range reapTicker {
		c.mu.Lock()
		timeAgo := time.Now().UTC().Add(-interval)
		for k, v := range c.entries {
			if v.createdAt.Before(timeAgo) {
				delete(c.entries, k)
			}
		}
		c.mu.Unlock()
	}
}
