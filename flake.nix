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
            go-tools # Static analysis tools

            # Python Development (using uv)
            uv
            python312 # Base interpreter for uv to use
          ];

          shellHook = ''
            # --- Python/uv Setup ---
            # Prevents uv from trying to manage its own Python binaries
            # which can cause issues on NixOS
            export UV_PYTHON_PREFERENCE="only-managed"
            export UV_PYTHON_INSTALL_DIR="${pkgs.python312}"

            echo "🚀 Learning Env Loaded!"
            echo "🐹 Go: $(go version)"
            echo "🐍 Python: $(python --version)"
            echo "⚡ uv: $(uv --version)"
          '';
        };
      });
    };
}
