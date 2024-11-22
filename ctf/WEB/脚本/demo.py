import hashlib
def md5_encode(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    md5_digest = md5_hash.hexdigest()
    return md5_digest

#md5(cookie_secret+md5(filename))
cookie_secert = "8e0ec61c-e16c-4ed2-a4ca-f51cd96f3efe"
res = md5_encode(cookie_secert+md5_encode("/fllllllllllllag"))
print(res)
