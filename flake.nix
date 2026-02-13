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
            # Go Development
            go
            gopls # Language Server
            gofumpt # Formatter
            go-tools # Static analysis tools
            delve # Debugger (DAP)
            golangci-lint # Linter (Recommended for Go extra)

            # Python Development (using uv)
            uv
            python312 # Base interpreter for uv to use
            pyright # LSP
            ruff # Linter & Formatter

            # SQL
            sqlite

            # Json
            vscode-langservers-extracted # LSPs for JSON, HTML, CSS
          ];

          shellHook = ''
            # --- Go Setup ---
            export GOPATH="$HOME/go"
            export PATH="$GOPATH/bin:$PATH"

            # --- Python/uv Setup ---
            export UV_PYTHON_PREFERENCE="only-managed"
            export UV_PYTHON_INSTALL_DIR="${pkgs.python312}"
          '';
        };
      });
    };
}
