{
  pkgs,
  ...
}:

{
  packages = with pkgs; [
    awscli2
  ];

  # https://devenv.sh/languages/
  languages = {
    go = {
      enable = true;
      delve = {
        enable = true;
      };
      lsp = {
        enable = true;
      };
    };
    terraform = {
      enable = true;
      lsp = {
        enable = true;
        package = pkgs.terraform-ls;
      };
    };
  };

  tasks = {
    "go:install-bootdev" = {
      exec = "go install github.com/bootdotdev/bootdev@latest";
      status = "command -v bootdev";
      before = [ "devenv:enterShell" ];
    };
  };

  enterShell = ''
    export MY_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    export MY_REGION=$(aws configure get region)

    echo "AWS Environment Loaded: $MY_REGION ($MY_ACCOUNT_ID)"
  '';
}
