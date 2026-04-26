{
  pkgs,
  ...
}:

{
  packages = [
    pkgs.ruff
  ];
  languages.python = {
    enable = true;
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
