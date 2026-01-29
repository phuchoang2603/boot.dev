{
  description = "Development environment for boot.dev with Go and Python";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};

        # Python with required packages
        pythonEnv = pkgs.python312.withPackages (
          ps: with ps; [
            google-genai
            python-dotenv
            pip
          ]
        );

        # Go environment
        goEnv = pkgs.buildGoModule {
          name = "boot-dev-go";
          src = ./13_go;
          vendorHash = null;
        };

      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            # Go toolchain
            go_1_25
            gopls
            go-tools

            # Python environment
            pythonEnv
            python312Packages.pip

            # Development tools
            git
            curl
            wget
            vim
          ];

          shellHook = ''
            echo "Welcome to the boot.dev development environment!"
            echo "Go version: $(go version)"
            echo "Python version: $(python --version)"
            echo ""
            echo "Available directories:"
            echo "  - 13_go/     : Go exercises and projects"
            echo "  - 08_proj_ai_agent/ : Python AI agent project"
            echo "  - Other Python projects in numbered directories"
            echo ""
            echo "To start developing:"
            echo "  - For Go: cd 13_go && go run ."
            echo "  - For Python: cd 08_proj_ai_agent && python main.py"
          '';
        };
      }
    );
}
