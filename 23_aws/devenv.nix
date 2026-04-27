{
  pkgs,
  ...
}:

{
  packages = with pkgs; [
    awscli2
  ];

  # https://devenv.sh/languages/
  languages.go = {
    enable = true;
    delve = {
      enable = true;
    };
    lsp = {
      enable = true;
    };
  };

  tasks = {
    "go:install-bootdev" = {
      exec = "go install github.com/bootdotdev/bootdev@latest";
      status = "command -v bootdev";
      before = [ "devenv:enterShell" ];
    };
  };
}
