### MD5长度扩展攻击

---

> 使用工具：https://github.com/luoingly/attack-scripts/blob/main/logic/md5-extension-attack.py

一道最近做的题，

```php
// 你以为这就结束了
if (!isset($_SESSION['random'])) {
    $_SESSION['random'] = bin2hex(random_bytes(16)) . bin2hex(random_bytes(16)) . bin2hex(random_bytes(16));
}

// 你想看到 random 的值吗?
// 你不是很懂 MD5 吗? 那我就告诉你他的 MD5 吧
$random = $_SESSION['random'];
echo md5($random);
echo '<br />';

$name = $_POST['name'] ?? 'user';

// check if name ends with 'admin'
if (substr($name, -5) !== 'admin') {
    die('不是管理员也来凑热闹?');
}

$md5 = $_POST['md5'];
if (md5($random . $name) !== $md5) {
    die('伪造? NO NO NO!');
}
```



我们可以观察到：

`$name`可控

`md(random)` 值已经知道了

变量`$_SESSION['random']` 的长度我们知道

因为知道了第一个字符串`$_SESSION['random']`的长度，我们可以构造第二个字符串`$random . $name`的值，也就是说我们手动在第二个字符串`$random . $name`的前端添加一些特定数据，使得第一轮计算因为我们添加数据后符合一轮计算的原数据长度而只计算出第一个字符串的hash值。这样我们就可以利用这个结果作为我们二轮计算的幻数进行下面的计算，从而预测最终的md结果。


例如，我们得到的md值：2580094662738492023445e5fdb0e1ed，我们的目的是添加一系列数据（最后五个字符是admin），使得加上random之后的md5与第一次md5值一样
> 关于这个变量`$_SESSION['random']` 的长度的计算：
> 1byte = 8 个字节
> 16byte=128个字节
> 4个二进制数等于一个16进制数
> 128/4*3=96

```python
[>] Input known text length: 96
[>] Input known hash: 2580094662738492023445e5fdb0e1ed
[>] Input append text: admin
[*] Attacking...
[+] Extend text: b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00admin'
[+] Extend text (URL encoded): %80%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%03%00%00%00%00%00%00admin
[+] Extend text (Base64): gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAABhZG1pbg==
[+] Final hash: 735f29b2def96d4978625c18ddc4fcae
```

这样`md5($random . $name)`加密之后的值也就等于`735f29b2def96d4978625c18ddc4fcae`

> 这样就实现了可以添加我们想要的内容去上面然后，满足题目的md5检测



md5算法--填充消息步骤：

MD5算法的第一步是对输入消息进行填充，使其长度满足一定的条件。具体步骤如下：

- **填充比特**：首先，在消息的末尾添加一个“1”比特。然后，在“1”比特之后添加若干个“0”比特，直到消息的长度满足以下条件：填充后的消息长度模512等于448。
- **附加长度**：在填充后的消息末尾附加一个64位的二进制数，表示原始消息的长度（以比特为单位）。如果原始消息的长度超过64位所能表示的范围，则只取其低64位。

填充和附加长度后，消息的总长度将是512的倍数。



#### md5_extension_attack脚本

```Python
from struct import pack, unpack
from math import floor, sin

class MD5:

    def __init__(self):
        self.A, self.B, self.C, self.D = \
            (0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476)  # initial values
        self.r: list[int] = \
            [7, 12, 17, 22] * 4 + [5,  9, 14, 20] * 4 + \
            [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4  # shift values
        self.k: list[int] = \
            [floor(abs(sin(i + 1)) * pow(2, 32))
             for i in range(64)]  # constants

    def _lrot(self, x: int, n: int) -> int:
        # left rotate
        return (x << n) | (x >> 32 - n)

    def update(self, chunk: bytes) -> None:
        # update the hash for a chunk of data (64 bytes)
        w = list(unpack('<'+'I'*16, chunk))
        a, b, c, d = self.A, self.B, self.C, self.D

        for i in range(64):
            if i < 16:
                f = (b & c) | ((~b) & d)
                flag = i
            elif i < 32:
                f = (b & d) | (c & (~d))
                flag = (5 * i + 1) % 16
            elif i < 48:
                f = (b ^ c ^ d)
                flag = (3 * i + 5) % 16
            else:
                f = c ^ (b | (~d))
                flag = (7 * i) % 16

            tmp = b + \
                self._lrot((a + f + self.k[i] + w[flag])
                           & 0xffffffff, self.r[i])
            a, b, c, d = d, tmp & 0xffffffff, b, c

        self.A = (self.A + a) & 0xffffffff
        self.B = (self.B + b) & 0xffffffff
        self.C = (self.C + c) & 0xffffffff
        self.D = (self.D + d) & 0xffffffff

    def extend(self, msg: bytes) -> None:
        # extend the hash with a new message (padded)
        assert len(msg) % 64 == 0
        for i in range(0, len(msg), 64):
            self.update(msg[i:i + 64])

    def padding(self, msg: bytes) -> bytes:
        # pad the message
        length = pack('<Q', len(msg) * 8)

        msg += b'\x80'
        msg += b'\x00' * ((56 - len(msg)) % 64)
        msg += length

        return msg

    def digest(self) -> bytes:
        # return the hash
        return pack('<IIII', self.A, self.B, self.C, self.D)


def verify_md5(test_string: bytes) -> None:
    # (DEBUG function) verify the MD5 implementation
    from hashlib import md5 as md5_hashlib

    def md5_manual(msg: bytes) -> bytes:
        md5 = MD5()
        md5.extend(md5.padding(msg))
        return md5.digest()

    manual_result = md5_manual(test_string).hex()
    hashlib_result = md5_hashlib(test_string).hexdigest()

    assert manual_result == hashlib_result, "Test failed!"


def attack(message_len: int, known_hash: str,
           append_str: bytes) -> tuple:
    # MD5 extension attack
    md5 = MD5()

    previous_text = md5.padding(b"*" * message_len)
    current_text = previous_text + append_str

    md5.A, md5.B, md5.C, md5.D = unpack("<IIII", bytes.fromhex(known_hash))
    md5.extend(md5.padding(current_text)[len(previous_text):])

    return current_text[message_len:], md5.digest().hex()


if __name__ == '__main__':

    message_len = int(input("[>] Input known text length: "))
    known_hash = input("[>] Input known hash: ").strip()
    append_text = input("[>] Input append text: ").strip().encode()

    print("[*] Attacking...")

    extend_str, final_hash = attack(message_len, known_hash, append_text)

    from urllib.parse import quote
    from base64 import b64encode

    print("[+] Extend text:", extend_str)
    print("[+] Extend text (URL encoded):", quote(extend_str))
    print("[+] Extend text (Base64):", b64encode(extend_str).decode())
    print("[+] Final hash:", final_hash)
```

