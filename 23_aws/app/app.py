import importlib
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def load_cmo_name() -> str | None:
    region = os.getenv("AWS_REGION") or os.getenv("AWS_DEFAULT_REGION") or "us-east-1"
    try:
        boto3 = importlib.import_module("boto3")
        ssm = boto3.client("ssm", region_name=region)
        result = ssm.get_parameter(Name="/CMO_NAME")
        value = result.get("Parameter", {}).get("Value", "").strip()
        return value or None
    except Exception:
        return None


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        cmo_name = load_cmo_name()
        if cmo_name:
            body = f"Hello from the container! From {cmo_name}."
        else:
            body = "Hello from the container!"

        payload = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()
