def detect(payload):
    signatures = ["http", "exe", "download"]

    for sig in signatures:
        if sig in payload.lower():
            return True
    return False
