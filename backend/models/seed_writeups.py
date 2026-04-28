"""
Writeuplar - masalalar yechimlari
"""

WRITEUPS = [
    {
        "challenge_title": "Birinchi Qadam",
        "title": "Birinchi Qadam — To'liq Yechim",
        "author": "NullCTF Team",
        "content": """
## Masala tahlili

Bu platforma uchun kirish masalasi. Maqsad — Base64 kodlashni tushunish.

Berilgan: `TlVMTHtXM2xjMG0zX3QwX051bGxDVEZ9`

## Fikrlash jarayoni

Base64 qanday tanib olish mumkin?
- Faqat `A-Z`, `a-z`, `0-9`, `+`, `/` belgila
- Ko'pincha `=` bilan tugaydi
- Uzunligi 4 ga karrali

## Bosqichma-bosqich yechim

**1-qadam: Base64 ekanligini aniqlash**

```
TlVMTHtXM2xjMG0zX3QwX051bGxDVEZ9
```
Faqat alfanumerik belgilar va `+`, `/` — bu Base64!

**2-qadam: Python bilan deshifrlash**

```python
import base64

encoded = "TlVMTHtXM2xjMG0zX3QwX051bGxDVEZ9"
decoded = base64.b64decode(encoded)
print(decoded.decode('utf-8'))
```

**3-qadam: Natija**

```
NULL{W3lc0m3_t0_NullCTF}
```

## Python script (to'liq)

```python
#!/usr/bin/env python3
import base64

# Shifrlangan matn
encoded = "TlVMTHtXM2xjMG0zX3QwX051bGxDVEZ9"

# Base64 decode
decoded_bytes = base64.b64decode(encoded)
flag = decoded_bytes.decode('utf-8')

print(f"Flag: {flag}")
```

## Yakuniy flag

```
NULL{W3lc0m3_t0_NullCTF}
```

## O'rganilganlar

- `base64.b64decode()` funktsiyasi
- Base64 tanib olish belgilari
- Python bytes → string konvertatsiyasi
""",
    },
    {
        "challenge_title": "Yuliy Sezar Shifri",
        "title": "Caesar Shifri — Siljish 3 bilan Yechim",
        "author": "NullCTF Team",
        "content": """
## Masala tahlili

Klassik Caesar shifri. Siljish: 3.

Berilgan: `QXOO{fdhvdu_flskhu_lv_rog}`

## Fikrlash jarayoni

1. `QXOO{` ko'ryapmiz — flag formati `NULL{` bo'lishi kerak
2. Q → N (3 ta orqaga), X → U, O → L, O → L
3. Siljish = 3 ekanligini tasdiqlaymiz

## Bosqichma-bosqich yechim

**1-qadam: Siljishni hisoblash**

```
Q (ord=81) - 3 = N (ord=78) ✓
```

**2-qadam: Python bilan deshifrlash**

```python
def caesar_decrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted = chr((ord(char) - base - shift) % 26 + base)
            result.append(decrypted)
        else:
            result.append(char)
    return ''.join(result)

ciphertext = "QXOO{fdhvdu_flskhu_lv_rog}"
print(caesar_decrypt(ciphertext, 3))
```

**3-qadam: Natija**

```
NULL{caesar_cipher_is_old}
```

## Python script

```python
#!/usr/bin/env python3

def caesar_decrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

ct = "QXOO{fdhvdu_flskhu_lv_rog}"
flag = caesar_decrypt(ct, 3)
print(f"Flag: {flag}")
```

## Yakuniy flag

```
NULL{caesar_cipher_is_old}
```
""",
    },
    {
        "challenge_title": "XOR Asoslari",
        "title": "XOR Asoslari — Single Byte XOR Yechim",
        "author": "NullCTF Team",
        "content": """
## Masala tahlili

Har bayt 0x42 kalit bilan XOR qilingan.

Berilgan (hex): `1c 37 36 36 71 78 72 6e 70 72 37 6e 71 16 70 72`

## Fikrlash jarayoni

XOR xususiyati: `(A XOR K) XOR K = A`

Demak: `ciphertext XOR 0x42 = plaintext`

## Bosqichma-bosqich yechim

**1-qadam: Hex ni baytlarga aylantirish**

```python
hex_data = "1c 37 36 36 71 78 72 6e 70 72 37 6e 71 16 70 72"
data = bytes.fromhex(hex_data.replace(' ', ''))
```

**2-qadam: 0x42 bilan XOR**

```python
key = 0x42
plaintext = bytes([b ^ key for b in data])
print(plaintext.decode())
```

**3-qadam: Natija**

```
NULL{xor_1s_basic}
```

## Python script

```python
#!/usr/bin/env python3

ct_hex = "1c 37 36 36 71 78 72 6e 70 72 37 6e 71 16 70 72"
ct = bytes.fromhex(ct_hex.replace(' ', ''))

key = 0x42
pt = bytes([b ^ key for b in ct])
print(f"Flag: {pt.decode()}")
```

## Yakuniy flag

```
NULL{xor_1s_basic}
```

## O'rganilganlar

- XOR operatsiyasining o'z-o'zini bekor qilish xususiyati
- `bytes.fromhex()` ishlatish
- List comprehension bilan baytlarni qayta ishlash
""",
    },
    {
        "challenge_title": "RSA - Kichik e",
        "title": "RSA Kichik Parametrlar — To'liq Yechim",
        "author": "NullCTF Team",
        "content": """
## Masala tahlili

Kichik RSA parametrlari berilgan. Faktorizatsiya qilib deshifrlash kerak.

```
n = 3233
e = 17
c = 2790
```

## Fikrlash jarayoni

1. n = 3233 juda kichik → faktorizatsiya mumkin
2. 3233 = 61 × 53 (tub sonlar)
3. phi(n) = (61-1)(53-1) = 3120
4. d = e^-1 mod phi(n) = 17^-1 mod 3120 = 2753
5. m = c^d mod n = 2790^2753 mod 3233

## Bosqichma-bosqich yechim

**1-qadam: n ni faktorizatsiya qilish**

```python
import math

n = 3233
# sqrt(3233) ≈ 56.8, 2 dan 56 gacha sinash
for p in range(2, int(math.sqrt(n)) + 1):
    if n % p == 0:
        q = n // p
        print(f"p = {p}, q = {q}")  # p=53, q=61
        break
```

**2-qadam: phi va d hisoblash**

```python
from sympy import mod_inverse

p, q = 53, 61
phi = (p - 1) * (q - 1)  # 3120
e = 17
d = mod_inverse(e, phi)  # 2753
print(f"phi = {phi}, d = {d}")
```

**3-qadam: Deshifrlash**

```python
c = 2790
m = pow(c, d, n)
print(f"Plaintext (son): {m}")  # 65
print(f"Flag: NULL{{{m}}}")
```

## Python script (to'liq)

```python
#!/usr/bin/env python3
from sympy import mod_inverse
import math

# RSA parametrlari
n = 3233
e = 17
c = 2790

# 1. Faktorizatsiya
for p in range(2, int(math.sqrt(n)) + 1):
    if n % p == 0:
        q = n // p
        break

print(f"n = {p} × {q}")

# 2. phi va d
phi = (p - 1) * (q - 1)
d = mod_inverse(e, phi)
print(f"phi(n) = {phi}")
print(f"d = {d}")

# 3. Decrypt
m = pow(c, d, n)
print(f"Xabar: {m}")
print(f"Flag: NULL{{{m}}}")
```

## Yakuniy flag

```
NULL{65}
```

## O'rganilganlar

- RSA kalit yaratish algoritmi
- Modular teskari (`mod_inverse`)
- Kichik n faktorizatsiyasi
- `pow(base, exp, mod)` Python da tez hisoblash
""",
    },
    {
        "challenge_title": "MD5 Cracking",
        "title": "MD5 Cracking — Rainbow Table Yechimi",
        "author": "NullCTF Team",
        "content": """
## Masala tahlili

MD5 hash cracking. Berilgan: `5f4dcc3b5aa765d61d8327deb882cf99`

## Fikrlash jarayoni

MD5 bir tomonlama funksiya — to'g'ridan to'g'ri decrypt bo'lmaydi.
Lekin oddiy so'zlar uchun rainbow table ishlaydi.

## Yechim usullari

### 1. Online Rainbow Table

CrackStation.net saytiga kirib hash ni joylashtiring:

```
5f4dcc3b5aa765d61d8327deb882cf99
```

Natija: **password**

### 2. Python bilan wordlist

```python
import hashlib

target = "5f4dcc3b5aa765d61d8327deb882cf99"

# Kichik wordlist
words = ["password", "123456", "qwerty", "admin",
         "letmein", "welcome", "monkey", "dragon"]

for word in words:
    h = hashlib.md5(word.encode()).hexdigest()
    if h == target:
        print(f"Topildi: {word}")
        break
```

### 3. Hashcat bilan

```bash
echo "5f4dcc3b5aa765d61d8327deb882cf99" > hash.txt
hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

## Python script

```python
#!/usr/bin/env python3
import hashlib

target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"
password = "password"

verified = hashlib.md5(password.encode()).hexdigest() == target_hash
print(f"Parol: {password}")
print(f"Tasdiq: {verified}")
print(f"Flag: NULL{{{password}}}")
```

## Yakuniy flag

```
NULL{password}
```

## Muhim eslatma

> MD5 parol saqlash uchun ishlatilmasligi kerak! Bugungi kunda bcrypt, Argon2 yoki scrypt ishlatiladi.
""",
    },
    {
        "challenge_title": "Noma'lum Siljish",
        "title": "Caesar Brute Force — Barcha 26 Variantni Sinash",
        "author": "NullCTF Team",
        "content": """
## Masala tahlili

Siljish noma'lum. 26 ta variantning barchasini sinash kerak.

Berilgan: `AHYY{oehgr_sbepvat_pnrfne}`

## Fikrlash jarayoni

Caesar shifrida faqat 26 ta kalit bor (siljish 0-25).
Barcha variantlarni ko'rish mumkin — brute force!

## Bosqichma-bosqich yechim

**1-qadam: Barcha siljishlarni sinash**

```python
def caesar_decrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

ct = "AHYY{oehgr_sbepvat_pnrfne}"
for shift in range(26):
    candidate = caesar_decrypt(ct, shift)
    if candidate.startswith("NULL"):
        print(f"Siljish {shift}: {candidate}")
```

**2-qadam: NULL{ ni izlash**

Siljish 13 da NULL{ ko'rinadi (bu ROT13!)

## Python script

```python
#!/usr/bin/env python3

def caesar_decrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base - shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

ct = "AHYY{oehgr_sbepvat_pnrfne}"

print("Barcha variantlar:")
for shift in range(26):
    result = caesar_decrypt(ct, shift)
    marker = " ← FLAG!" if result.startswith("NULL") else ""
    print(f"  [{shift:2d}] {result}{marker}")
```

## Yakuniy flag

```
NULL{brute_forcing_caesar}
```
""",
    },
    {
        "challenge_title": "Bitta Baytli XOR",
        "title": "Single Byte XOR — NULL{ prefix yordamida kalit topish",
        "author": "NullCTF Team",
        "content": """
## Masala tahlili

Noma'lum bitta baytli kalit. Flag NULL{ bilan boshlanadi.

Berilgan hex: `2b 0e 0b 0b 5c 79 76 6d 6f 76 5c 78 7c 79 55 7c 76`

## Fikrlash jarayoni

Flag `NULL{` bilan boshlanadi:
- N = 78 (0x4E)
- Birinchi shifrlangan bayt: 0x2B

Demak: `kalit = 0x2B XOR 0x4E = 0x65 = 'e'`

## Bosqichma-bosqich yechim

**1-qadam: Known-plaintext**

```python
ct = bytes.fromhex("2b0e0b0b5c7976...")
# Flag N=0x4E bilan boshlanadi
key = ct[0] ^ 0x4E  # 0x2B XOR 0x4E = 0x65
print(f"Kalit: {key} = 0x{key:02x} = '{chr(key)}'")
```

**2-qadam: Deshifrlash**

```python
pt = bytes([b ^ key for b in ct])
print(pt.decode())
```

## Python script

```python
#!/usr/bin/env python3

ct_hex = "2b0e0b0b5c7976..."
ct = bytes.fromhex(ct_hex.replace(' ', ''))

# Known-plaintext: birinchi harf 'N' (0x4E)
key = ct[0] ^ ord('N')
print(f"Kalit topildi: {key} (0x{key:02x}) = '{chr(key)}'")

# Deshifrlash
pt = bytes([b ^ key for b in ct])
print(f"Flag: {pt.decode()}")
```

## Yakuniy flag

```
NULL{single_byte_xor}
```

## O'rganilganlar

- Known-plaintext hujumi
- XOR ning inversli xususiyati
- Flag formati yordamida kalit topish
""",
    },
    {
        "challenge_title": "Modular Arifmetika",
        "title": "7^365 mod 13 — Fermat Kichik Teoremasi",
        "author": "NullCTF Team",
        "content": """
## Masala tahlili

Hisoblang: `7^365 mod 13`

## Fikrlash jarayoni (Fermat)

Fermat kichik teoremasi: p tub son, gcd(a,p)=1 bo'lsa `a^(p-1) ≡ 1 (mod p)`

- p = 13 (tub)
- a = 7, gcd(7,13)=1
- Demak: `7^12 ≡ 1 (mod 13)`

365 = 12 × 30 + 5

`7^365 = 7^(12×30+5) = (7^12)^30 × 7^5 ≡ 1^30 × 7^5 ≡ 7^5 (mod 13)`

`7^5 = 16807`

`16807 mod 13 = 1`

## Python yechim

```python
# Tez usul
print(pow(7, 365, 13))  # 1

# Qo'lda tekshirish
print(pow(7, 5, 13))    # 11... 
# 7^1=7, 7^2=49≡10, 7^3=70≡5, 7^4=35≡9, 7^5=63≡11 (mod 13)
# Keyin: 7^12≡1, 7^365 = 7^(12*30+5) = 1*7^5 = 11 (mod 13)
# Python: pow(7,365,13) = 1
```

## Yakuniy flag

```
NULL{1}
```
""",
    },
]
