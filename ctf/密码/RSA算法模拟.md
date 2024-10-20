# 数论以及模拟RSA

[TOC]



## 基本学习

### 欧拉定理

如果 \( n \) 是一个正整数，且 \( a \) 是一个与 \( n \) 互质的整数，那么：
$$
a^{\phi(n)} \equiv 1 \pmod{n}
$$
其中
$$
\phi(n)
$$
是欧拉函数，表示小于 n 的正整数中与  n 互质的数的个数



### 费马小定理

如果p是一个素数，且 a是一个整数，且a不被p整除（即a和p互质），那么：
$$
a^{p-1} \equiv 1 \pmod{p}
$$


### 快速幂算法

速幂算法（也称为“二进制指数算法”或“平方乘法算法”）是一种高效计算  
$$
a^{b} \pmod{m}
$$
的算法。该算法通过将指数 b 转换为二进制表示，并利用平方和乘法操作，将计算复杂度从线性降低到对数级别



- **将指数 b转为二进制**：

$$
b_k b_{k-1} \cdots b_1 b_0
$$

- **初始化结果**：

$$
\text{result} = 1
$$

$$
\text{result} = (\text{result} \times \text{result}) \mod m
\text{result} = (\text{result} \times a) \mod m
$$

$$
b = 1101_2
\text{result} = (1 \times 3) \mod 11 = 3
\text{base} = (3 \times 3) \mod 11 = 9
b = 110_2
b = 110_2
\text{base} = (9 \times 9) \mod 11 = 4
b = 11_2
\text{result} = (3 \times 4) \mod 11 = 12 \mod 11 = 1
\text{base} = (4 \times 4) \mod 11 = 16 \mod 11 = 5
b = 1_2
\text{result} = (1 \times 5) \mod 11 = 5
\text{base} = (5 \times 5) \mod 11 = 25 \mod 11 = 3
b = 0_2
$$



### Wilson定理

如果  是一个素数，那么：
$$
(p-1)! \equiv -1 \pmod{p}
$$
反过来，如果n 是一个大于 1 的正整数，并且：
$$
(n-1)! \equiv -1 \pmod{n}
$$


那么n  一定是素数。





### 模逆元：

#### 概念

对于给定的整数 \( a \) 和模数 \( m \)，如果存在一个整数 \( b \) 满足以下条件：
$$
a \times b \equiv 1 \pmod{m} \
$$
则称 \( b \) 是 \( a \) 模 \( m \) 的逆元，计为
$$
a^{-1}\equiv b\pmod{m}
$$
 (b)是一个整数,使得(a)  乘以 (b) 再取模(m)  后的结果为 1。

`Python` 实现：

```python
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
```

1. **基本情况**：
   $$
   \gcd(3, 11) = 1
   $$

2. **递归步骤**：
   $$
   11 = 3 \times 3 + 2 \quad \Rightarrow \quad \gcd(3, 2)
   3 = 2 \times 1 + 1 \quad \Rightarrow \quad \gcd(2, 1)
   2 = 1 \times 2 + 0 \quad \Rightarrow \quad \gcd(1, 0) = 1
   $$ {LaTeX}
   
3. **回溯**：
   $$
   1 = 3 - 2 \times 1
   $$

   $$
   2 = 11 - 3 \times 3
   $$

   代入上式：
   $$
   1 = 3 - (11 - 3 \times 3) \times 1
   $$

   $$
   1 = 3 - 11 + 3 \times 3
   $$

   $$
   1 = 3 \times 4 - 11
   $$

   因此，x = 4  是 \( 3 \) 模 \( 11 \) 的逆元。

4. **验证**：
   $$
   3 \times 4 = 12 \equiv 1 \pmod{11}
   $$
   

所以，\( 3 \) 模 \( 11 \) 的逆元是 \( 4 \)。



#### 使用快速幂算法

假设我们要计算 \( 3 \) 模 \( 11 \) 的逆元，且 \( 11 \) 是一个素数。

1. **使用费马小定理**：
   $$
   3^{11-2} \equiv 3^9 \pmod{11}\
   $$
   
2. **快速幂算法**：
   $$
   3^9 = 3 \times (3^4)^2
   $$

$$
3^2 = 9
$$

$$
3^4 = 9^2 = 81 \equiv 4 \pmod{11}
$$

$$
3^8 = 4^2 = 16 \equiv 5 \pmod{11}
$$

$$
3^9 = 3 \times 5 = 15 \equiv 4 \pmod{11}
$$

所以，\( 3 \) 模 \( 11 \) 的逆元是 \( 4 \)。



### 扩展欧几里得算法（贝祖等式）

$$
ax + by = \text{gcd}(a, b)
$$

**算法流程：**

1. 基本情况：如果 \( b = 0 \)，则
   $$
   {gcd}(a, b) = a，
   $$
   此时 x = 1, y = 0 ,因为
   $$
    a \times 1 + b \times 0 = a 
   $$
   
2. 递归步骤：如果b!=0 ，递归地计算gcd(b,a%b)  以及相应的  x'和y'

3. 更新x和y：根据递归返回的结果，更新  x 和  y 的值。具体来说，如果:
   $$
   ax' + by' = \text{gcd}(a, b)
   $$
   则可以通过以下方式更新  x 和  y ：
   $$
   x = y', 
   y = x' - \left\lfloor \frac{a}{b} \right\rfloor \times y'
   $$
   

   其中,[a/b]表示  a 除以  b 的商（向下取整）。

```python
#python
import sys
def extended_gcd(a, b):
    #终止递归的条件
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

sys.stdout.reconfigure(encoding='utf-8')
# 示例
a = 35
b = 15
gcd, x, y = extended_gcd(a, b)
print(f"对于 a = {a} 和 b = {b}:")
print(f"最大公约数 gcd = {gcd}")
print(f"x = {x}, y = {y}")
print(f"验证: {a} * {x} + {b} * {y} = {gcd}")
```

输出结果如下：

```python
对于 a = 35 和 b = 15:
最大公约数 gcd = 5
x = 1, y = -2
验证: 35 * 1 + 15 * -2 = 5
```

我们可以手工走一遍：

![image-20241017101923620](https://gitee.com/bx33661/image/raw/master/path/image-20241017101923620.png)

![image-20241017101945677](https://gitee.com/bx33661/image/raw/master/path/image-20241017101945677.png)

### 



### 使用方法：
- 运行代码后，会生成一个256位的RSA密钥对，并使用该密钥对对消息进行加密和解密。
- 你可以调整 `key_size` 来增加或减少密钥的长度，从而影响安全性。

### 注意：
- 这个实现是一个简单的演示，不适合用于生产环境。实际应用中，RSA密钥长度通常为2048位或更高，并且需要处理更大的整数和更复杂的数学运算。
- 在实际应用中，建议使用成熟的加密库（如`cryptography`）来处理RSA加密。



运行结果：

```
Public Key: (2459061735167995563465226723142653612310725461667945402049490894306966926731, 2665407292140973978164142669121776922665974332724182091598737802804110690709)
Private Key: (580140555277896844331256081646360671964456059651682932657357893332173884731, 2665407292140973978164142669121776922665974332724182091598737802804110690709)
Encrypted Message: [1356958432366854625286857949848651283278738137746020091692418120871064638932, 2566817238945006870263995080398546562259537248112185122539650799857645495497, 94020645424703033028072100951405324830958086683584293644281034610245758627, 94020645424703033028072100951405324830958086683584293644281034610245758627, 1254999537848042891783949322892667564555404546071350168894758477931258073917, 1426135808129362040823613826171319239505160094798465024226262396284953604521, 1735094508227161135588622429284914867503543817303312380466189282102905999578, 2045279851726961009490112015282195629450008859390589847568963730503736277669, 1221782813198555949831227667767468799746921459936094448738075607033628322516, 408502188591225994531006270715965822323909574962389570310653988200770569721, 316417480868069060835295522079761899086620529124026657855926822606017637984]
Decrypted Message: Hello, RSA!
```



## RSA算法模拟

### Python实现

RSA（Rivest-Shamir-Adleman）是一种非对称加密算法，广泛用于加密和数字签名。下面是一个简单的Python实现，展示了RSA算法的基本原理。

```python
import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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

def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

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
```

代码说明：

1. **gcd(a, b)**: 计算两个数的最大公约数。
2. **mod_inverse(a, m)**: 计算模逆元，即找到一个数 `x` 使得 `(a * x) % m = 1`。
3. **is_prime(n)**: 使用Miller-Rabin素性测试来判断一个数是否为素数。
4. **generate_prime(bits)**: 生成一个指定比特长度的素数。
5. **generate_keypair(key_size)**: 生成RSA密钥对，包括公钥和私钥。
6. **encrypt(public_key, plaintext)**: 使用公钥加密明文。
7. **decrypt(private_key, ciphertext)**: 使用私钥解密密文。

### RSA原理

RSA（Rivest-Shamir-Adleman）是一种非对称加密算法，广泛用于加密和数字签名。它的安全性基于大整数分解的困难性。下面是RSA算法的详细原理：

### 1. 密钥生成
RSA算法的第一步是生成公钥和私钥。具体步骤如下：

#### 1.1 选择两个大素数 `p` 和 `q`
选择两个大素数 `p` 和 `q`。这两个素数越大，RSA算法越安全，但计算开销也越大。

#### 1.2 计算 `n`
计算 `n = p * q`。`n` 是公钥和私钥的模数。

#### 1.3 计算欧拉函数 `φ(n)`
欧拉函数 `φ(n)` 表示小于 `n` 且与 `n` 互质的正整数的个数。对于两个素数 `p` 和 `q`，有：
\[ φ(n) = (p - 1) * (q - 1) \]

#### 1.4 选择公钥 `e`
选择一个整数 `e`，使得 `1 < e < φ(n)`，并且 `e` 与 `φ(n)` 互质（即 `gcd(e, φ(n)) = 1`）。通常选择 `e = 65537`，因为它是一个常用的素数，且计算效率较高。

#### 1.5 计算私钥 `d`
计算 `d`，使得 `d` 是 `e` 对 `φ(n)` 的模逆元，即：
\[ d * e ≡ 1 \mod φ(n) \]
这意味着存在一个整数 `k`，使得：
\[ d = (1 + k * φ(n)) / e \]

### 2. 加密
假设要加密的消息是 `m`，加密过程如下：

#### 2.1 使用公钥 `(e, n)` 加密
加密公式为：
\[ c = m^e \mod n \]
其中 `c` 是加密后的密文。

### 3. 解密
假设接收到的密文是 `c`，解密过程如下：

#### 3.1 使用私钥 `(d, n)` 解密
解密公式为：
\[ m = c^d \mod n \]
其中 `m` 是解密后的明文。

### 4. 数学原理
RSA算法的安全性基于大整数分解的困难性。具体来说，如果攻击者能够分解 `n` 得到 `p` 和 `q`，那么他就可以计算出 `φ(n)`，进而计算出私钥 `d`。然而，对于足够大的 `n`，分解 `n` 是非常困难的，因此RSA算法是安全的。

### 5. 数字签名
RSA算法还可以用于数字签名。具体步骤如下：

#### 5.1 签名
使用私钥 `(d, n)` 对消息 `m` 进行签名：
\[ s = m^d \mod n \]
其中 `s` 是签名。

#### 5.2 验证签名
使用公钥 `(e, n)` 对签名 `s` 进行验证：
\[ m' = s^e \mod n \]
如果 `m'` 等于原始消息 `m`，则签名有效。