{
  pkgs,
  lib,
  config,
  ...
}:

let
  db_user = "postgres";
  db_pass = "postgres";
  db_name = "chirpy";
  db_host = "127.0.0.1";
  db_port = "5432";
in
{
  packages = with pkgs; [
    sqlc
    sqls
    sqruff
    goose
  ];

  languages.go = {
    enable = true;
    delve.enable = true;
    lsp.enable = true;
  };

  files.".sqruff".ini = {
    sqruff = {
      dialect = "postgres";
    };
  };

  files."config.yml".yaml = {
    lowercaseKeywords = false;
    connections = [
      {
        alias = "local_postgres";
        driver = "postgresql";
        proto = "tcp";
        user = db_user;
        passwd = db_pass;
        host = db_host;
        port = lib.toInt db_port;
        dbName = db_name;
        params = {
          sslmode = "disable";
        };
      }
    ];
  };

  services.postgres = {
    enable = true;
    package = pkgs.postgresql_16;
    listen_addresses = db_host;
    port = lib.toInt db_port;
    initialDatabases = [
      {
        name = db_name;
        user = db_user;
        pass = db_pass;
      }
    ];
    settings = {
      log_connections = true;
      log_statement = "all";
      max_connections = 100;
    };
  };

  tasks."db:migrate" = {
    exec = "goose -dir sql/schema postgres \"$DB_URL\" up";
    after = [ "devenv:processes:postgres@ready" ];
    before = [ "devenv:processes:web" ];
  };

  processes.web = {
    ports.http.allocate = 8080;
    exec = "go run . --port ${toString config.processes.web.ports.http.value}";
    watch = {
      paths = [ ./. ];
      extensions = [
        "go"
        "sql"
        "yaml"
      ];
      ignore = [
        ".devenv"
        "vendor"
      ];
    };
    restart.on = "always";
  };

  env.DB_URL = "postgres://${db_user}:${db_pass}@${db_host}:${db_port}/${db_name}?sslmode=disable";
  scripts.migrate.exec = "goose -dir sql/schema postgres \"$DB_URL\" up";
}
