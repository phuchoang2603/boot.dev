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
    version = "3.12";
    venv.enable = true;
    lsp = {
      enable = true;
      package = pkgs.ty;
    };
  };
}
