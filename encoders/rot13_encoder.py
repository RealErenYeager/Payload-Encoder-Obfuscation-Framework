import codecs

def encode(payload):
    return codecs.encode(payload, 'rot_13')
