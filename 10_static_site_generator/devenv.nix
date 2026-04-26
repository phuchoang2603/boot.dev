{
  pkgs,
  ...
}:

{
  packages = [
    pkgs.ruff
    pkgs.python312Packages.pytest
    pkgs.python312Packages.debugpy
  ];
  languages.python = {
    enable = true;
    directory = "./src";
    version = "3.12";
    venv.enable = true;
    uv = {
      enable = true;
      sync.enable = true;
    };
    lsp = {
      enable = true;
      package = pkgs.ty;
    };
  };
}
