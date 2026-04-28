def lambda_handler(event, context):
    request_context = event.get("requestContext", {})
    identity = request_context.get("identity", {})
    ip_address = identity.get("sourceIp")
    if not ip_address:
        headers = event.get("headers", {})
        ip_address = headers.get("X-Forwarded-For") or headers.get("x-forwarded-for")
    if not ip_address:
        ip_address = "unknown"
    print(f"Received IP: {ip_address}")
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/plain",
        },
        "body": f"Your IP address is: {ip_address}",
    }
