{
  config,
  ...
}:

{
  languages.go = {
    enable = true;
    delve.enable = true;
    lsp.enable = true;
  };
  processes.web = {
    ports.http.allocate = 8899;
    exec = "go run . --port ${toString config.processes.web.ports.http.value}";
    watch = {
      paths = [ ./. ];
      extensions = [
        "go"
      ];
      ignore = [
        ".devenv"
        "*.log"
        "vendor"
      ];
    };
    restart.on = "always";
  };
  env = {
    LINKO_LOG_FILE = "linko.access.log";
    OTEL_EXPORTER_OTLP_TRACES_INSECURE = "true";
  };
}
