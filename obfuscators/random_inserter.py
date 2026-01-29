import random
import string

def obfuscate(payload):
    result = ""
    for c in payload:
        result += c
        if random.random() < 0.2:
            result += random.choice(string.ascii_letters)
    return result
