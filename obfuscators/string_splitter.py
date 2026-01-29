def obfuscate(payload):
    return "+".join([f"'{c}'" for c in payload])
