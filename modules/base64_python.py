import base64


def encode(text):
    byte_text = text.encode()
    byte_encoded_text = base64.b64encode(byte_text)
    encoded_text = byte_encoded_text.decode(errors='ignore')
    return encoded_text


def crack(encoded_text):
    byte_encoded_text = encoded_text.encode()
    byte_decoded_text = base64.b64decode(byte_encoded_text)
    decoded_text = byte_decoded_text.decode(errors='ignore')
    return decoded_text
