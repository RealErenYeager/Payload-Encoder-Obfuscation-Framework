from encoders.base64_encoder import encode as b64
from obfuscators.random_inserter import obfuscate
from detection.signature_checker import detect
from reports.report_generator import generate

with open("samples/payload.txt") as f:
    payload = f.read()

encoded = b64(payload)
obfuscated = obfuscate(encoded)
detected = detect(obfuscated)

generate(payload, obfuscated, detected)
