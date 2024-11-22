hex_string = "627833333636312d6c6574277320676f21"

decode_string = bytes.fromhex(hex_string).decode("utf-8")

print(decode_string)