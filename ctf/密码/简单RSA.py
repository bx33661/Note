import random

#计算最大公约数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#计算模逆元
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

#判断是否为质数
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Miller-Rabin primality test
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

def generate_keypair(key_size):
    p = generate_prime(key_size // 2)
    q = generate_prime(key_size // 2)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Compute the modular inverse of e
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

# 编码
def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]
# 解码
def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)

if __name__ == "__main__":
    key_size = 256  # You can adjust the key size for security
    public_key, private_key = generate_keypair(key_size)

    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    message = "Hello, RSA!"
    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")
