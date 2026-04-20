package main

import "testing"

func Test_redactIP(t *testing.T) {
	tests := []struct {
		name string // description of this test case
		// Named input parameters for target function.
		hostport string
		want     string
	}{
		{
			name:     "IPv4 address with port",
			hostport: "192.168.1.1:8080",
			want:     "192.168.1.x",
		},
		{
			name:     "Local IPv6 address with port",
			hostport: "[::1]:8080",
			want:     "127.0.0.x",
		},
		{
			name:     "Invalid hostport format",
			hostport: "invalid_hostport",
			want:     "invalid_hostport",
		},
		{
			name:     "Non-IP host with port",
			hostport: "example.com:8080",
			want:     "example.com",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := redactIP(tt.hostport)
			if got != tt.want {
				t.Errorf("redactIP() = %v, want %v", got, tt.want)
			}
		})
	}
}
