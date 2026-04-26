{
  pkgs,
  lib,
  ...
}:

let
  db_user = "postgres";
  db_pass = "postgres";
  db_name = "gator";
  db_host = "127.0.0.1";
  db_port = "5432";
in
{
  packages = with pkgs; [
    sqlc
    sqls
    goose
  ];

  languages.go = {
    enable = true;
    delve.enable = true;
    lsp.enable = true;
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

  files."compose.yaml".yaml = {
    services.db = {
      image = "postgres:16";
      container_name = "blog-db";
      environment = {
        POSTGRES_USER = db_user;
        POSTGRES_PASSWORD = db_pass;
        POSTGRES_DB = db_name;
      };
      volumes = [ "db_data:/var/lib/postgresql/data" ];
      ports = [ "${db_port}:5432" ];
    };
    volumes.db_data = { };
  };

  files.".gatorconfig.json".json = {
    db_url = "postgres://${db_user}:${db_pass}@${db_host}:${db_port}/${db_name}?sslmode=disable";
  };

  env.DB_URL = "postgres://${db_user}:${db_pass}@${db_host}:${db_port}/${db_name}?sslmode=disable";
  scripts.migrate.exec = "goose -dir sql/schema postgres \"$DB_URL\" up";
}
