{
  description = "Modernized Go and Python (uv) learning environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      # Define supported systems
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      # Helper to generate outputs for all systems
      forAllSystems =
        f:
        nixpkgs.lib.genAttrs systems (
          system:
          f (
            import nixpkgs {
              inherit system;
              config.allowUnfree = true;
            }
          )
        );
    in
    {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          packages = with pkgs; [
            # --- Custom Build Scripts ---
            (pkgs.writeShellScriptBin "go-build-linux" ''
              CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build "$@"
            '')

            # Go Development
            go
            gopls # Language Server
            gofumpt # Formatter
            go-tools # Static analysis tools
            govulncheck # Vulnerability checker
            delve # Debugger

            # Python Development (using uv)
            uv
            python312 # Base interpreter for uv to use
            ty # LSP
            ruff # Linter & Formatter
            python312Packages.pytest
            python312Packages.debugpy

            # SQL
            sqlite
            goose
            sqlc

            # For S3 course
            ffmpeg

            # For CICD course
            turso-cli
          ];

          shellHook = ''
            # --- Go Setup ---
            export GOPATH="$HOME/go"
            export PATH="$GOPATH/bin:$PATH"

            # --- Python/uv Setup ---
            export UV_PYTHON="$(which python3)"
            export UV_PYTHON_INSTALL_DIR="$HOME/.local/share/uv/python"
            export UV_PYTHON_PREFERENCE="only-system"
          '';
        };
      });
    };
}
