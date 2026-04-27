{
  pkgs,
  config,
  ...
}:

let
  rabbit_user = "guest";
  rabbit_pass = "guest";
in
{
  services.rabbitmq = {
    enable = true;
    package = pkgs.rabbitmq-server;

    managementPlugin = {
      enable = true;
      port = 15672;
    };

    port = 5672;

    configItems = {
      "default_user" = rabbit_user;
      "default_pass" = rabbit_pass;
      "load_definitions" = "./definitions.json";
    };
  };

  env.AMQP_URL =
    let
      port = toString config.processes.rabbitmq.ports.main.value;
    in
    "amqp://${rabbit_user}:${rabbit_pass}@localhost:${port}/";

  languages.go = {
    enable = true;
    delve.enable = true;
    lsp.enable = true;
  };

  scripts = {
    run-server.exec = "go run ./cmd/server";
    run-client.exec = "go run ./cmd/client";
  };
}
