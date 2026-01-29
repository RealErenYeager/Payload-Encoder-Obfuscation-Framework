def encode(payload, key=5):
    encoded = ''.join(chr(ord(c) ^ key) for c in payload)
    return encoded
