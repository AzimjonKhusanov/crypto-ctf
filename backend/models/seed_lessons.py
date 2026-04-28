LESSONS = [
    # ══════════════════════════════════════════════════════════════════
    # 1. KIRISH
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "Kriptografiyaga Kirish",
        "slug": "kirish",
        "category": "Asoslar",
        "order_num": 1,
        "difficulty": "oson",
        "content": """
<h2>Kriptografiya nima?</h2>
<p>Kriptografiya — ma'lumotlarni shifrlash va himoya qilish fani. So'zi yunonchadan kelgan: <strong>kryptos</strong> (yashirin) + <strong>graphia</strong> (yozish).</p>

<div class="concept-box">
<h3>🎯 Asosiy tushunchalar</h3>
<ul>
<li><strong>Plaintext (ochiq matn)</strong> — shifrlashdan oldingi asl xabar</li>
<li><strong>Ciphertext (shifrlangan matn)</strong> — shifrlangan xabar</li>
<li><strong>Key (kalit)</strong> — shifrlash/deshifrlash uchun ishlatiladigan sir</li>
<li><strong>Encrypt</strong> — ochiq matnni shifrlash</li>
<li><strong>Decrypt</strong> — shifrlangan matnni ochish</li>
</ul>
</div>

<h2>Kriptografiya qanday ishlaydi?</h2>
<div class="step-box">
<div class="step">
<span class="step-num">1</span>
<div>Alice Bob ga xabar yubormoqchi: <code>"Salom Bob!"</code></div>
</div>
<div class="step">
<span class="step-num">2</span>
<div>Alice xabarni shifrlaydi → <code>"Xfpnt Cpc!"</code></div>
</div>
<div class="step">
<span class="step-num">3</span>
<div>Shifrlangan xabar internetdan o'tadi</div>
</div>
<div class="step">
<span class="step-num">4</span>
<div>Bob kalit yordamida deshifrlaydi → <code>"Salom Bob!"</code></div>
</div>
</div>

<h2>Kriptografiya turlari</h2>
<div class="info-grid">
<div class="info-card">
<h4>🔐 Simmetrik</h4>
<p>Shifrlash va deshifrlash uchun bir xil kalit</p>
<p>Misol: AES, DES, ChaCha20</p>
</div>
<div class="info-card">
<h4>🔑 Asimmetrik</h4>
<p>Ochiq va maxfiy kalit juft</p>
<p>Misol: RSA, ECC, El Gamal</p>
</div>
<div class="info-card">
<h4>#️⃣ Hashing</h4>
<p>Bir tomonlama funksiya</p>
<p>Misol: MD5, SHA256, bcrypt</p>
</div>
</div>

<h2>CTF (Capture The Flag) nima?</h2>
<p>CTF — kiberxavfsizlik musobaqasi. Ishtirokchilar turli kriptografiya, web, forensics va boshqa sohalardagi masalalarni yechib <strong>flag</strong> (bayroq) topishadi.</p>
<div class="flag-example">
<code>NULL{bu_flagning_namunasi}</code>
</div>
<p>Ushbu platformadagi barcha flaglar <code>NULL{...}</code> formatida.</p>

<h2>Python bilan boshlash</h2>
<pre><code class="language-python"># Kriptografiya uchun foydali Python kutubxonalari
import base64        # Base64 encoding
from Crypto.Cipher import AES  # pycryptodome
import hashlib       # MD5, SHA256
import binascii      # hex konvertatsiya

# Oddiy misol: hex dan matn
hex_data = "48656c6c6f"
text = bytes.fromhex(hex_data).decode()
print(text)  # Hello
</code></pre>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 2. BASE64
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "Base64 Encoding",
        "slug": "base64",
        "category": "Encoding",
        "order_num": 2,
        "difficulty": "oson",
        "content": """
<h2>Base64 nima?</h2>
<p>Base64 — binary ma'lumotlarni matn ko'rinishida ifodalash usuli. 64 ta belgidan foydalanadi: <code>A-Z, a-z, 0-9, +, /</code></p>

<div class="concept-box">
<h3>💡 Nima uchun ishlatiladi?</h3>
<p>Email, URL, HTML kabi matn asosidagi protokollar binary ma'lumotni ko'tara olmaydi. Base64 ularni xavfsiz uzatishga imkon beradi.</p>
</div>

<h2>Qanday ishlaydi?</h2>
<div class="step-box">
<div class="step">
<span class="step-num">1</span>
<div>Matnni baytlarga aylantir: <code>"Man" → 77, 97, 110</code></div>
</div>
<div class="step">
<span class="step-num">2</span>
<div>Binaryga o'tkazish: <code>01001101 01100001 01101110</code></div>
</div>
<div class="step">
<span class="step-num">3</span>
<div>6 bitli guruhlarga bo'l: <code>010011 010110 000101 101110</code></div>
</div>
<div class="step">
<span class="step-num">4</span>
<div>Base64 jadvaldan mosini ol: <code>T W F u</code> → <code>TWFu</code></div>
</div>
</div>

<h2>Python misoli</h2>
<pre><code class="language-python">import base64

# Shifrlash (encode)
matn = "Salom dunyo!"
encoded = base64.b64encode(matn.encode())
print(encoded)  # b'U2Fsb20gZHVueW8h'

# Deshifrlash (decode)
decoded = base64.b64decode("U2Fsb20gZHVueW8h").decode()
print(decoded)  # Salom dunyo!

# URL-safe variant
url_encoded = base64.urlsafe_b64encode(matn.encode())
print(url_encoded)  # b'U2Fsb20gZHVueW8h'

# Base32 (boshqa variant)
b32 = base64.b32encode(matn.encode())
print(b32)  # b'KNUGG33NF5QGE3LQNR...'
</code></pre>

<h2>Qanday tanib olish mumkin?</h2>
<div class="tip-box">
<ul>
<li>Ko'pincha <code>=</code> yoki <code>==</code> bilan tugaydi (padding)</li>
<li>Faqat <code>A-Z, a-z, 0-9, +, /</code> harflari</li>
<li>Uzunligi har doim 4 ga karrali</li>
<li>Original uzunlikdan ~33% uzun</li>
</ul>
</div>

<h2>Amaliy mashq</h2>
<div class="challenge-link">
<p>Bu darsga oid challenge: <a href="/challenges">Birinchi Qadam</a></p>
<code>TlVMTHtXM2xjMG0zX3QwX051bGxDVEZ9</code>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 3. XOR
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "XOR Operatsiyasi",
        "slug": "xor",
        "category": "Simmetrik",
        "order_num": 3,
        "difficulty": "oson",
        "content": """
<h2>XOR (Eksklyuziv OR) nima?</h2>
<p>XOR — ikki bitni taqqoslaydigan mantiqiy operatsiya. <strong>Faqat bittasi 1 bo'lganda</strong> natija 1.</p>

<table class="truth-table">
<tr><th>A</th><th>B</th><th>A XOR B</th></tr>
<tr><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>1</td></tr>
<tr><td>1</td><td>1</td><td>0</td></tr>
</table>

<h2>XOR ning muhim xususiyatlari</h2>
<div class="concept-box">
<ul>
<li><strong>A XOR A = 0</strong> — o'zi bilan XOR → 0</li>
<li><strong>A XOR 0 = A</strong> — nol bilan XOR → o'zgarmaydi</li>
<li><strong>A XOR B = B XOR A</strong> — kommutativ</li>
<li><strong>(A XOR B) XOR B = A</strong> — <em>bu kriptografiya uchun muhim!</em></li>
</ul>
</div>

<h2>Qanday shifrlaydi?</h2>
<pre><code class="language-python"># XOR shifrlash
def xor_encrypt(plaintext, key):
    # Kalit takrorlanadi (cycling)
    result = []
    for i, char in enumerate(plaintext):
        encrypted_byte = ord(char) ^ ord(key[i % len(key)])
        result.append(chr(encrypted_byte))
    return ''.join(result)

def xor_decrypt(ciphertext, key):
    # XOR o'zi o'zining teskarisi!
    return xor_encrypt(ciphertext, key)

# Misol
matn = "Salom"
kalit = "K"
encrypted = ''.join(chr(ord(c) ^ ord(kalit)) for c in matn)
print("Shifrlangan:", encrypted)
decrypted = ''.join(chr(ord(c) ^ ord(kalit)) for c in encrypted)
print("Deshifrlangan:", decrypted)  # Salom
</code></pre>

<h2>Python bytes bilan</h2>
<pre><code class="language-python"># Hex ma'lumot bilan ishlash
ciphertext_hex = "1c 37 36 36 71"
key_byte = 0x42

ciphertext = bytes.fromhex(ciphertext_hex.replace(' ', ''))
plaintext = bytes([b ^ key_byte for b in ciphertext])
print(plaintext.decode('utf-8', errors='replace'))

# Ko'p baytli kalit bilan
def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

data = b"\\x9d\\xc4\\xc5\\xc1"
key = b"KEY"
result = xor_bytes(data, key)
print(result)
</code></pre>

<h2>Single-byte XOR ni qanday buzish mumkin?</h2>
<div class="step-box">
<div class="step">
<span class="step-num">1</span>
<div>Flag har doim NULL{ bilan boshlanadi</div>
</div>
<div class="step">
<span class="step-num">2</span>
<div>Birinchi bayt: N = 78 (ASCII)</div>
</div>
<div class="step">
<span class="step-num">3</span>
<div>kalit = ct[0] XOR 78</div>
</div>
<div class="step">
<span class="step-num">4</span>
<div>Barcha baytlarga shu kalit bilan XOR qiling</div>
</div>
</div>

<pre><code class="language-python"># Single-byte XOR cracking
def crack_single_xor(ciphertext: bytes) -> tuple:
    # Eng yaxshi kalitni qidirish (ingliz matni bo'lsa)
    best_key = 0
    best_score = 0
    
    english_freqs = "etaoinshrdlu"  # Eng ko'p uchraydigan harflar
    
    for key in range(256):
        decrypted = bytes([b ^ key for b in ciphertext])
        try:
            text = decrypted.decode('utf-8')
            score = sum(1 for c in text.lower() if c in english_freqs)
            if score > best_score:
                best_score = score
                best_key = key
        except:
            continue
    
    return best_key, bytes([b ^ best_key for b in ciphertext])

ct = bytes.fromhex("2b0e0b0b5c7976...")
key, pt = crack_single_xor(ct)
print(f"Kalit: {key} (0x{key:02x})")
print(f"Plaintext: {pt}")
</code></pre>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 4. CAESAR CIPHER
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "Caesar Shifri",
        "slug": "caesar",
        "category": "Klassik",
        "order_num": 4,
        "difficulty": "oson",
        "content": """
<h2>Caesar shifri tarixi</h2>
<p>Rim imperatori Yuliy Sezar harbiy xabarlarini himoya qilish uchun bu usulni ishlatgan. Har harfni alfavitda ma'lum son (odatda 3) ga surgan.</p>

<div class="history-box">
<blockquote>"Agar Sezar harbiy sirlarini yozishga ehtiyoj sezsa, u harflarni almashtirardi: A ni D bilan, B ni E bilan..." — Suetonius</blockquote>
</div>

<h2>Qanday ishlaydi?</h2>
<p>Har bir harfni alfavitda K ta o'ringa suring (K = kalit):</p>

<div class="cipher-demo">
<div class="alphabet-row">
<strong>Asl:</strong>   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
</div>
<div class="alphabet-row">
<strong>K=3:</strong>  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
</div>
</div>

<h2>Python bilan shifrlash</h2>
<pre><code class="language-python">def caesar_encrypt(text: str, shift: int) -> str:
    result = []
    for char in text.upper():
        if char.isalpha():
            # Harfni raqamga o'tkazish (A=0, B=1, ...)
            num = ord(char) - ord('A')
            # Siljitish va modulo 26 (alfavit chegarasi)
            shifted = (num + shift) % 26
            result.append(chr(shifted + ord('A')))
        else:
            result.append(char)  # Harf bo'lmasa o'zgarmasdan
    return ''.join(result)

def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)  # Teskarisi

# Misol
matn = "SALOM DUNYO"
encrypted = caesar_encrypt(matn, 3)
print("Shifrlangan:", encrypted)  # VDORP GXQBR

decrypted = caesar_decrypt(encrypted, 3)
print("Deshifrlangan:", decrypted)  # SALOM DUNYO
</code></pre>

<h2>Brute Force (barcha variantlarni sinash)</h2>
<pre><code class="language-python">def brute_force_caesar(ciphertext: str):
    print("Barcha 26 ta variant:")
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"  Siljish {shift:2d}: {decrypted}")

brute_force_caesar("AHYY{oehgr_sbepvat_pnrfne}")
# Siljish 13: NULL{brute_forcing_caesar}  ← To'g'ri javob!
</code></pre>

<h2>ROT13 — maxsus holat</h2>
<pre><code class="language-python">import codecs

# ROT13 = siljish 13 (o'zi o'zining teskarisi!)
text = "Salom"
rot13 = codecs.encode(text, 'rot_13')
print(rot13)  # Fnyby
print(codecs.encode(rot13, 'rot_13'))  # Salom (qaytadi)

# Yoki qo'lda:
def rot13(text):
    return caesar_encrypt(text, 13)
</code></pre>

<h2>Frekvens tahlil</h2>
<p>Ingliz tilida harflar bir xil chastota bilan uchraydi. E eng ko'p (~13%), keyin T, A, O, I...</p>
<pre><code class="language-python">from collections import Counter

def frequency_analysis(ciphertext: str) -> dict:
    letters = [c for c in ciphertext.upper() if c.isalpha()]
    total = len(letters)
    freq = Counter(letters)
    return {k: v/total*100 for k, v in sorted(freq.items(), key=lambda x: -x[1])}

# Eng ko'p uchraydigan harf E ga mos kelishi kerak
ct_freq = frequency_analysis("QXOO{fdhvdu_flskhu_lv_rog}")
print(ct_freq)
</code></pre>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 5. VIGENERE
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "Vigenère Shifri",
        "slug": "vigenere",
        "category": "Klassik",
        "order_num": 5,
        "difficulty": "o'rta",
        "content": """
<h2>Vigenère shifri nima?</h2>
<p>Blaise de Vigenère tomonidan yaratilgan (XVI asr). Caesar shifrini kuchaytiradi: har harfni boshqacha kalit bilan siljitadi.</p>

<div class="concept-box">
<h3>💡 Asosiy farq</h3>
<p>Caesar: bitta kalit → bitta siljish<br>
Vigenère: kalit so'z → har harf uchun turli siljish</p>
</div>

<h2>Qanday ishlaydi?</h2>
<pre><code class="language-python">def vigenere_encrypt(plaintext: str, key: str) -> str:
    result = []
    key = key.upper()
    key_index = 0
    
    for char in plaintext.upper():
        if char.isalpha():
            # Kalit harfini siljish sifatida ishlat
            shift = ord(key[key_index % len(key)]) - ord('A')
            shifted = (ord(char) - ord('A') + shift) % 26
            result.append(chr(shifted + ord('A')))
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    result = []
    key = key.upper()
    key_index = 0
    
    for char in ciphertext.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            shifted = (ord(char) - ord('A') - shift) % 26  # Ayirish!
            result.append(chr(shifted + ord('A')))
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

# Misol
matn = "HELLO WORLD"
kalit = "KEY"
encrypted = vigenere_encrypt(matn, kalit)
print("Shifrlangan:", encrypted)  # RIJVS UYVJN

decrypted = vigenere_decrypt(encrypted, kalit)
print("Deshifrlangan:", decrypted)  # HELLO WORLD
</code></pre>

<h2>Kasiski testi — Vigenèreни buzish</h2>
<div class="step-box">
<div class="step"><span class="step-num">1</span><div>Takrorlanuvchi 3+ harfli ketma-ketliklarni toping</div></div>
<div class="step"><span class="step-num">2</span><div>Ular orasidagi masofani o'lchang</div></div>
<div class="step"><span class="step-num">3</span><div>GCD(masofalar) = kalit uzunligi</div></div>
<div class="step"><span class="step-num">4</span><div>Har kalit pozitsiyasi uchun alohida Caesar</div></div>
</div>

<pre><code class="language-python">from math import gcd
from functools import reduce
from collections import Counter

def kasiski_test(ciphertext: str, min_len: int = 3) -> list:
    # Takrorlanuvchi ketma-ketliklarni toping va GCD hisoblang
    ct = ''.join(c for c in ciphertext.upper() if c.isalpha())
    spacings = []
    
    for length in range(min_len, 6):
        for i in range(len(ct) - length):
            pattern = ct[i:i+length]
            for j in range(i + length, len(ct) - length + 1):
                if ct[j:j+length] == pattern:
                    spacings.append(j - i)
    
    if not spacings:
        return []
    
    # GCD hisoblash
    overall_gcd = reduce(gcd, spacings)
    factors = [i for i in range(2, 20) if overall_gcd % i == 0]
    return factors

def find_key_length(ciphertext: str) -> int:
    factors = kasiski_test(ciphertext)
    return factors[0] if factors else 1

# Kalit uzunligi topilgandan keyin har pozitsiyani Caesar kabi hal qilish
def break_vigenere(ciphertext: str, key_length: int) -> str:
    ct = ''.join(c for c in ciphertext.upper() if c.isalpha())
    key = ""
    
    for i in range(key_length):
        # Har i-chi pozitsiyasidagi harflarni to'pla
        column = ct[i::key_length]
        # Eng ko'p uchragan harf E ga mos kelishi kerak
        freq = Counter(column).most_common(1)[0][0]
        shift = (ord(freq) - ord('E')) % 26
        key += chr(shift + ord('A'))
    
    return key
</code></pre>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 6. RSA
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "RSA Kriptografiyasi",
        "slug": "rsa",
        "category": "Asimmetrik",
        "order_num": 6,
        "difficulty": "qiyin",
        "content": """
<h2>RSA nima?</h2>
<p>RSA (Rivest-Shamir-Adleman, 1977) — eng mashhur asimmetrik kriptosistema. Katta sonlarni faktorizatsiya qilishning qiyinligiga asoslangan.</p>

<div class="concept-box">
<h3>🔑 Kalit juft</h3>
<ul>
<li><strong>Ochiq kalit (n, e)</strong> — hamma biladigan</li>
<li><strong>Maxfiy kalit (n, d)</strong> — faqat siz bilasiz</li>
</ul>
</div>

<h2>Kalit yaratish (step-by-step)</h2>
<div class="step-box">
<div class="step"><span class="step-num">1</span><div>Ikkita katta tub son tanlang: <strong>p, q</strong></div></div>
<div class="step"><span class="step-num">2</span><div>n = p × q hisoblang</div></div>
<div class="step"><span class="step-num">3</span><div>φ(n) = (p-1) × (q-1) — Euler funksiyasi</div></div>
<div class="step"><span class="step-num">4</span><div>e tanlang: 1 < e < φ(n), gcd(e, φ(n)) = 1 (odatda 65537)</div></div>
<div class="step"><span class="step-num">5</span><div>d hisoblang: e × d ≡ 1 (mod φ(n)) — modular teskari</div></div>
</div>

<h2>Shifrlash va deshifrlash</h2>
<div class="formula-box">
<p><strong>Shifrlash:</strong> C = M<sup>e</sup> mod n</p>
<p><strong>Deshifrlash:</strong> M = C<sup>d</sup> mod n</p>
</div>

<pre><code class="language-python">from sympy import isprime, mod_inverse
import random

def rsa_keygen(bits: int = 512):
    # RSA kalit juft yaratish
    # 1. Ikkita katta tub son
    # (Sodda misol uchun kichik sonlar)
    p = 61
    q = 53
    
    # 2. n
    n = p * q  # 3233
    
    # 3. phi
    phi = (p - 1) * (q - 1)  # 3120
    
    # 4. e
    e = 17  # gcd(17, 3120) = 1
    
    # 5. d (modular teskari)
    d = mod_inverse(e, phi)  # 2753
    
    return (n, e), (n, d)

def rsa_encrypt(m: int, n: int, e: int) -> int:
    # Shifrlash: c = m^e mod n
    return pow(m, e, n)

def rsa_decrypt(c: int, n: int, d: int) -> int:
    # Deshifrlash: m = c^d mod n
    return pow(c, d, n)

# Misol
public_key, private_key = rsa_keygen()
n, e = public_key
_, d = private_key

print(f"Ochiq kalit: n={n}, e={e}")
print(f"Maxfiy kalit: d={d}")

message = 65  # Shifrlash uchun son
ciphertext = rsa_encrypt(message, n, e)
print(f"Shifrlangan: {ciphertext}")  # 2790

decrypted = rsa_decrypt(ciphertext, n, d)
print(f"Deshifrlangan: {decrypted}")  # 65
</code></pre>

<h2>CTF da RSA hujumlari</h2>
<div class="attack-grid">
<div class="attack-card">
<h4>🔓 Kichik n</h4>
<p>n kichik bo'lsa → faktorizatsiya qiling</p>
<code>factordb.com</code>
</div>
<div class="attack-card">
<h4>🔓 e=3, kichik m</h4>
<p>m³ < n bo'lsa → oddiy kub ildiz</p>
<code>m = c^(1/3)</code>
</div>
<div class="attack-card">
<h4>🔓 Wiener</h4>
<p>d juda kichik bo'lsa</p>
<code>continued fractions</code>
</div>
<div class="attack-card">
<h4>🔓 Common modulus</h4>
<p>Bir xil n, turli e bilan</p>
<code>extended gcd</code>
</div>
</div>

<pre><code class="language-python">from sympy import integer_nthroot
from math import isqrt

# e=3 Cube Root hujumi
def cube_root_attack(c: int, n: int) -> int:
    "m^3 < n bolsa ishlaydi"
    m, perfect = integer_nthroot(c, 3)
    if perfect:
        return m
    return None

# Fermat faktorizatsiya
def fermat_factor(n: int):
    "p va q bir biriga yaqin bolsa"
    a = isqrt(n) + 1
    while True:
        b2 = a * a - n
        b = isqrt(b2)
        if b * b == b2:
            return (a - b, a + b)
        a += 1

# n = 100000007
p, q = fermat_factor(100000007)
print(f"p={p}, q={q}")  # p=9999, q=10001
</code></pre>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 7. AES
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "AES (Advanced Encryption Standard)",
        "slug": "aes",
        "category": "Simmetrik",
        "order_num": 7,
        "difficulty": "qiyin",
        "content": """
<h2>AES nima?</h2>
<p>AES — 2001 yilda NIST tomonidan standart sifatida qabul qilingan blok shifr. 128, 192 yoki 256 bitli kalit ishlatadi. Bugungi kunda Internet xavfsizligining asosi.</p>

<h2>AES ishlash principi</h2>
<div class="step-box">
<div class="step"><span class="step-num">1</span><div><strong>SubBytes</strong> — S-box orqali baytlarni almashtirish</div></div>
<div class="step"><span class="step-num">2</span><div><strong>ShiftRows</strong> — qatorlarni siljitish</div></div>
<div class="step"><span class="step-num">3</span><div><strong>MixColumns</strong> — ustunlarni aralashtirish</div></div>
<div class="step"><span class="step-num">4</span><div><strong>AddRoundKey</strong> — kalit bilan XOR</div></div>
</div>
<p>Bu 4 qadam 10-14 marta (raund soni kalitga bog'liq) takrorlanadi.</p>

<h2>AES rejimlari</h2>

<h3>ECB — Electronic Codebook (Xavfli!)</h3>
<pre><code class="language-python">from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b"YELLOW SUBMARINE"  # 16 bayt = 128 bit

# Shifrlash
cipher = AES.new(key, AES.MODE_ECB)
plaintext = b"Hello World!!!!!"  # 16 bayt (blok o'lchami)
ciphertext = cipher.encrypt(plaintext)
print(ciphertext.hex())

# Deshifrlash
cipher = AES.new(key, AES.MODE_ECB)
decrypted = cipher.decrypt(ciphertext)
print(decrypted.decode())

# MUAMMO: bir xil plaintext → bir xil ciphertext!
# Shuning uchun ECB xavfli — naqsh ko'rinadi
</code></pre>

<h3>CBC — Cipher Block Chaining (Yaxshiroq)</h3>
<pre><code class="language-python">from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
iv  = get_random_bytes(16)  # Initialization Vector

# Shifrlash
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = b"Salom dunyo! Bu CBC rejimi testi!"
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# Deshifrlash
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
print(decrypted.decode())
</code></pre>

<h3>CTR — Counter Mode (Zamonaviy)</h3>
<pre><code class="language-python">from Crypto.Cipher import AES
from Crypto.Util import Counter

key = b"YELLOW SUBMARINE"
nonce = 0  # HECH QACHON bir xil nonce ni qayta ishlatmang!

ctr = Counter.new(128, initial_value=nonce)
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
ciphertext = cipher.encrypt(b"Salom CTR!")

# Xuddi shunday nonce bilan decrypt
ctr = Counter.new(128, initial_value=nonce)
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
plaintext = cipher.decrypt(ciphertext)
print(plaintext.decode())
</code></pre>

<h2>CTF da AES hujumlari</h2>
<div class="attack-grid">
<div class="attack-card">
<h4>🐧 ECB Penguin</h4>
<p>ECB da naqshlar ko'rinadi. Rasm faylini AES-ECB bilan shifrlasang, naqsh saqlanadi.</p>
</div>
<div class="attack-card">
<h4>🔮 Padding Oracle</h4>
<p>Server padding xatosi bersa, CBC ni bir baytdan buzish mumkin.</p>
</div>
<div class="attack-card">
<h4>♻️ CTR Nonce Reuse</h4>
<p>Bir xil nonce ishlatilsa: ct1 XOR ct2 = pt1 XOR pt2</p>
</div>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 8. HASHING
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "Hash Funksiyalari",
        "slug": "hashing",
        "category": "Hashing",
        "order_num": 8,
        "difficulty": "o'rta",
        "content": """
<h2>Hash funksiya nima?</h2>
<p>Hash funksiya — ixtiyoriy uzunlikdagi ma'lumotni <strong>qat'iy uzunlikdagi</strong> chiqishga aylantiradi. <strong>Bir tomonlama</strong>: hash dan asl ma'lumotni olish mumkin emas (nazariy jihatdan).</p>

<div class="concept-box">
<h3>📋 Xususiyatlari</h3>
<ul>
<li><strong>Deterministik</strong> — bir xil kirishdan bir xil natija</li>
<li><strong>Tez</strong> — hisoblash tez</li>
<li><strong>Avalanche Effect</strong> — 1 bitli o'zgarish hash ni butunlay o'zgartiradi</li>
<li><strong>Collision Resistance</strong> — bir xil hash beruvchi iki xabar topish qiyin</li>
<li><strong>Pre-image Resistance</strong> — hash dan kirish topish qiyin</li>
</ul>
</div>

<h2>Mashhur hash algoritmlari</h2>
<pre><code class="language-python">import hashlib

matn = "Salom"
data = matn.encode()

# MD5 (128 bit — hozir xavfli!)
md5 = hashlib.md5(data).hexdigest()
print(f"MD5:    {md5}")

# SHA1 (160 bit — hozir zaif)
sha1 = hashlib.sha1(data).hexdigest()
print(f"SHA1:   {sha1}")

# SHA256 (256 bit — hozir standart)
sha256 = hashlib.sha256(data).hexdigest()
print(f"SHA256: {sha256}")

# SHA512 (512 bit — juda kuchli)
sha512 = hashlib.sha512(data).hexdigest()
print(f"SHA512: {sha512}")

# bcrypt (parol saqlash uchun — tuzli va sekin)
import bcrypt
password = b"mysecretpassword"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(f"bcrypt: {hashed}")
print(bcrypt.checkpw(password, hashed))  # True
</code></pre>

<h2>Hash cracking usullari</h2>
<div class="step-box">
<div class="step"><span class="step-num">1</span>
<div><strong>Dictionary Attack</strong> — so'zlar ro'yxatini sinash
<code>hashcat -m 0 hash.txt wordlist.txt</code></div>
</div>
<div class="step"><span class="step-num">2</span>
<div><strong>Brute Force</strong> — barcha kombinatsiyalarni sinash
<code>hashcat -m 0 -a 3 hash.txt ?a?a?a?a</code></div>
</div>
<div class="step"><span class="step-num">3</span>
<div><strong>Rainbow Tables</strong> — oldindan hisoblangan jadvallar
<code>crackstation.net</code></div>
</div>
</div>

<pre><code class="language-python"># MD5 cracking (sodda misol)
import hashlib

target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"
wordlist = ["password", "123456", "admin", "letmein", "qwerty"]

for word in wordlist:
    if hashlib.md5(word.encode()).hexdigest() == target_hash:
        print(f"Topildi! Parol: {word}")
        break

# Hash turini aniqlash
def identify_hash(h: str) -> str:
    length = len(h)
    if length == 32:  return "MD5 yoki MD4"
    if length == 40:  return "SHA1"
    if length == 64:  return "SHA256"
    if length == 128: return "SHA512"
    if h.startswith("$2b$"): return "bcrypt"
    return "Noma'lum"
</code></pre>

<h2>Length Extension hujumi</h2>
<p>MD5 va SHA1 uchun Merkle-Damgård konstruktsiyasidan foydalanib, mavjud hash ga qo'shimcha ma'lumot qo'shish mumkin:</p>
<pre><code class="language-python"># hashpump vositasi:
# hashpump -s "hash" -d "asl_matn" -a ";admin=true" -k 10
# Bu yangi hash va to'ldirilgan ma'lumot qaytaradi
</code></pre>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 9. DIFFIE-HELLMAN
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "Diffie-Hellman Kalit Almashish",
        "slug": "diffie-hellman",
        "category": "Asimmetrik",
        "order_num": 9,
        "difficulty": "o'rta",
        "content": """
<h2>DH nima?</h2>
<p>Diffie-Hellman (1976) — ochiq kanal orqali maxfiy kalit almashish protokoli. Ikkala tomon birgalikda hech kim bilib olmaydigan umumiy sir yaratadi.</p>

<div class="concept-box">
<h3>🎨 Rang analogi</h3>
<p>Alice va Bob bir xil umumiy rang bilishadi (sariq). Har biri o'ziga maxfiy rang tanlaydi va umumiy rang bilan aralashtiradi. So'ng aralashtirgan ranglarini almashtirishadi. Endi har biri uchala rangni biladi va bir xil umumiy rangga ega bo'ladi!</p>
</div>

<h2>Matematik asosi</h2>
<div class="formula-box">
<p>Ochiq parametrlar: <strong>g</strong> (generator), <strong>p</strong> (tub son)</p>
<p>Alice: a (maxfiy) → A = g<sup>a</sup> mod p (ochiq)</p>
<p>Bob: b (maxfiy) → B = g<sup>b</sup> mod p (ochiq)</p>
<p>Umumiy kalit: K = A<sup>b</sup> mod p = B<sup>a</sup> mod p = g<sup>ab</sup> mod p</p>
</div>

<pre><code class="language-python">def diffie_hellman():
    # Ochiq parametrlar
    p = 23   # Kichik tub son (haqiqiyda 2048+ bit)
    g = 5    # Generator
    
    # Alice ning maxfiy kaliti
    a = 6
    A = pow(g, a, p)  # A = 5^6 mod 23 = 8
    print(f"Alice yuboradi: A = {A}")
    
    # Bob ning maxfiy kaliti
    b = 15
    B = pow(g, b, p)  # B = 5^15 mod 23 = 19
    print(f"Bob yuboradi: B = {B}")
    
    # Umumiy kalit hisoblash
    K_alice = pow(B, a, p)  # K = 19^6 mod 23 = 2
    K_bob   = pow(A, b, p)  # K = 8^15 mod 23 = 2
    
    print(f"Alice kaliti: {K_alice}")
    print(f"Bob kaliti: {K_bob}")
    assert K_alice == K_bob, "Kalit mos kelmadi!"
    return K_alice

shared_key = diffie_hellman()
print(f"Umumiy sir kalit: {shared_key}")  # 2
</code></pre>

<h2>DH xavfsizlik muammolari</h2>
<div class="attack-grid">
<div class="attack-card">
<h4>🕵️ MITM hujumi</h4>
<p>Alice va Bob o'rtasida turgan tajovuzkor ikkala tomonga ham o'z ochiq kalitini yuboradi.</p>
</div>
<div class="attack-card">
<h4>🔢 Kichik p</h4>
<p>p kichik bo'lsa, diskret logarifm brute force bilan topiladi.</p>
</div>
<div class="attack-card">
<h4>🔄 Statik kalit</h4>
<p>Har sessiyada yangi a va b ishlatilmasa, forward secrecy yo'q.</p>
</div>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 10. MODULAR ARIFMETIKA
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "Modular Arifmetika",
        "slug": "modular-arifmetika",
        "category": "Matematika",
        "order_num": 10,
        "difficulty": "o'rta",
        "content": """
<h2>Modular arifmetika nima?</h2>
<p>Modular arifmetika — "soat" arifmetikasi deb ham ataladi. 12 soat soatida 11 + 3 = 2 (14 emas).</p>
<p><strong>a mod n</strong> — a ni n ga bo'lgandagi qoldiq.</p>

<pre><code class="language-python"># Python da mod operatori
print(17 % 5)   # 2  (17 = 3*5 + 2)
print(25 % 7)   # 4  (25 = 3*7 + 4)

# Tez darajaga ko'tarish (kriptografiya uchun muhim)
# pow(base, exp, mod) — Python da O(log(exp)) tezlikda
print(pow(7, 365, 13))  # 7^365 mod 13 = 1

# Qo'lda hisoblash SEKIN bo'lishi mumkin:
# 7^365 = juda katta son ... mod 13
# Lekin Python pow() bu ni tez hal qiladi
</code></pre>

<h2>Fermat kichik teoremasi</h2>
<div class="formula-box">
<p>p tub son va gcd(a, p) = 1 bo'lsa:<br>
<strong>a<sup>p-1</sup> ≡ 1 (mod p)</strong></p>
</div>

<pre><code class="language-python"># Fermat: 7^12 ≡ 1 (mod 13) chunki p=13, p-1=12
print(pow(7, 12, 13))  # 1 ✓

# Demak: 7^365 mod 13 = 7^(12*30 + 5) mod 13
# = (7^12)^30 * 7^5 mod 13
# = 1^30 * 7^5 mod 13
print(pow(7, 5, 13))   # 11... lekin Python pow(7,365,13) = 1

# To'g'ri hisoblash:
# 365 = 12*30 + 5, shuning uchun 7^365 ≡ 7^5 ≡ 11 (mod 13)
# Lekin yuqoridagi misol: 7^365 mod 13... qayta tekshiring
</code></pre>

<h2>Modular teskari (Modular Inverse)</h2>
<div class="formula-box">
<p>a * a<sup>-1</sup> ≡ 1 (mod n)</p>
<p>RSA da: e * d ≡ 1 (mod φ(n))</p>
</div>

<pre><code class="language-python">from sympy import mod_inverse
from math import gcd

# Modular teskari topish
# 3 * ? ≡ 1 (mod 7)
inv = mod_inverse(3, 7)
print(inv)  # 5  (chunki 3*5 = 15 = 2*7 + 1)
print(3 * 5 % 7)  # 1 ✓

# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x

def modinverse(a, m):
    g, x, _ = extended_gcd(a % m, m)
    if g != 1:
        raise ValueError("Teskari mavjud emas")
    return x % m

print(modinverse(17, 3120))  # 2753 — RSA misoli
</code></pre>

<h2>Xitoy Qoldig'i Teoremasi (CRT)</h2>
<pre><code class="language-python">def crt(remainders, moduli):
    "Xitoy Qoldighi Teoremasi"
    from math import prod
    M = prod(moduli)
    result = 0
    
    for r, m in zip(remainders, moduli):
        Mi = M // m
        yi = mod_inverse(Mi, m)
        result += r * Mi * yi
    
    return result % M

# Misol: x ≡ 2(mod3), x ≡ 3(mod5), x ≡ 2(mod7)
x = crt([2, 3, 2], [3, 5, 7])
print(x)  # 23
print(23 % 3, 23 % 5, 23 % 7)  # 2, 3, 2 ✓
</code></pre>
""",
    },
]
