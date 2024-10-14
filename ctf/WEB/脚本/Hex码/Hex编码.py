need_string = "ffifdyop"
byte_string = need_string.encode("utf-8")
encode_string = bytes.hex(byte_string)
print(encode_string)