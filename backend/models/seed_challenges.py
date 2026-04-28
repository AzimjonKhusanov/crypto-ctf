"""
Kriptografiya masalalari - 50+ ta challenge
"""

CHALLENGES = [
    # ══════════════════════════════════════════════
    # ENCODING KATEGORIYASI
    # ══════════════════════════════════════════════
    {
        "title": "Birinchi Qadam",
        "description": """Salom, yangi CTF o'yinchisi! Bu eng oson masala.
Quyidagi matni Base64 orqali deshifrlang:
<code>TlVMTHtXM2xjMG0zX3QwX051bGxDVEZ9</code>
Flagni toping va yuboring!""",
        "category": "Encoding",
        "difficulty": "oson",
        "points": 50,
        "flag": "NULL{W3lc0m3_t0_NullCTF}",
        "hint": "Python: import base64; base64.b64decode('...')",
    },
    {
        "title": "Hex Siri",
        "description": """Bu qator hex (o'n oltilik) kodda yashiringan:
<code>4e554c4c7b6830785f31735f33617379217d</code>
Deshifrlang va flagni toping.""",
        "category": "Encoding",
        "difficulty": "oson",
        "points": 50,
        "flag": "NULL{h0x_1s_3asy!}",
        "hint": "Python: bytes.fromhex('...')",
    },
    {
        "title": "Binary Til",
        "description": """Kompyuterlar faqat 0 va 1 ni tushunadi. Ushbu binary qatorni deshifrlang:
<code>01001110 01010101 01001100 01001100 01111011 01100010 00110001 01101110 00110100 01110010 01111001 01111101</code>""",
        "category": "Encoding",
        "difficulty": "oson",
        "points": 75,
        "flag": "NULL{b1n4ry}",
        "hint": "Har 8 bitni ASCII belgiga aylantiring",
    },
    {
        "title": "Rot13 Jumboq",
        "description": """Bu oddiy o'rin almashtirish shifri. Deshifrlang:
<code>AHYY{ebg_guvegrra_vf_sha}</code>""",
        "category": "Encoding",
        "difficulty": "oson",
        "points": 50,
        "flag": "NULL{rot_thirteen_is_fun}",
        "hint": "Har harf 13 ta oldinga surilgan",
    },
    {
        "title": "URL Encoding",
        "description": """Veb sahifalar URL da maxsus belgilarni kodlaydi. Quyidagini deshifrlang:
<code>%4e%55%4c%4c%7b%75%72%6c%5f%65%6e%63%30%64%31%6e%67%7d</code>""",
        "category": "Encoding",
        "difficulty": "oson",
        "points": 75,
        "flag": "NULL{url_enc0d1ng}",
        "hint": "Python: urllib.parse.unquote('%...')",
    },
    {
        "title": "Base32 Jumboq",
        "description": """Base64 dan farqli o'laroq, Base32 faqat 32 ta belgidan foydalanadi:
<code>JZQW4ZLTEBQXEZJAN5ZGK3TFOQQGS3TF</code>""",
        "category": "Encoding",
        "difficulty": "o'rta",
        "points": 100,
        "flag": "NULL{base32_decoded}",
        "hint": "Python: import base64; base64.b32decode('...')",
    },
    {
        "title": "ASCII Art Siri",
        "description": """Bu ASCII qiymatlar ro'yxatini belgiga aylantirang:
<code>78 85 76 76 123 97 115 99 49 49 95 49 115 95 102 117 110 125</code>""",
        "category": "Encoding",
        "difficulty": "oson",
        "points": 50,
        "flag": "NULL{asc11_1s_fun}",
        "hint": "Python: chr(78) → 'N'",
    },
    {
        "title": "Morse Kodi",
        "description": """Klassik telegraf kodini hal qiling:
<code>-. ..- .-.. .-.. { -- --- .-. ... . } </code>""",
        "category": "Encoding",
        "difficulty": "oson",
        "points": 75,
        "flag": "NULL{morse}",
        "hint": "Morse kodi: A=.-, B=-..., ...",
    },

    # ══════════════════════════════════════════════
    # CAESAR / CLASSICAL KATEGORIYASI
    # ══════════════════════════════════════════════
    {
        "title": "Yuliy Sezar Shifri",
        "description": """Yuliy Sezar o'z xabarlarini yuborish uchun bu usuldan foydalangan.
Siljish: 3
<code>QXOO{fdhvdu_flskhu_lv_rog}</code>
Deshifrlang!""",
        "category": "Caesar",
        "difficulty": "oson",
        "points": 75,
        "flag": "NULL{caesar_cipher_is_old}",
        "hint": "Har harfni 3 ta orqaga suring",
    },
    {
        "title": "Noma'lum Siljish",
        "description": """Bu safar siljish noma'lum. Barcha 26 ta variantni sinab ko'ring:
<code>AHYY{oehgr_sbepvat_pnrfne}</code>""",
        "category": "Caesar",
        "difficulty": "oson",
        "points": 100,
        "flag": "NULL{brute_forcing_caesar}",
        "hint": "26 ta siljishni sinab ko'ring",
    },
    {
        "title": "ROT47 Shifri",
        "description": """ROT13 ning kuchaytirilgan versiyasi - harflar va belgilarni o'zgartiradi:
<code>}F{{Lr%E@w6X0X_r@C_4Fd6{</code>""",
        "category": "Caesar",
        "difficulty": "o'rta",
        "points": 150,
        "flag": "NULL{rot47_includes_symbols}",
        "hint": "ROT47: ASCII 33-126 oraliqidagi belgilar aylanadi",
    },
    {
        "title": "Atbash Shifri",
        "description": """Qadimgi ibroniy shifri - alfavit teskari tartibda ishlatiladi (A=Z, B=Y, ...):
<code>MFOO{zgyzhs_xrksvi}</code>""",
        "category": "Caesar",
        "difficulty": "o'rta",
        "points": 125,
        "flag": "NULL{atbash_cipher}",
        "hint": "A<->Z, B<->Y, C<->X, ...",
    },

    # ══════════════════════════════════════════════
    # XOR KATEGORIYASI
    # ══════════════════════════════════════════════
    {
        "title": "XOR Asoslari",
        "description": """XOR - kriptografiyaning asosi. Ushbu hex qiymatni 0x42 kalit bilan XOR qiling:
<code>1c 37 36 36 71 78 72 6e 70 72 37 6e 71 16 70 72</code>
Natija flag bo'ladi.""",
        "category": "XOR",
        "difficulty": "o'rta",
        "points": 150,
        "flag": "NULL{xor_1s_basic}",
        "hint": "Python: bytes([b ^ 0x42 for b in bytes.fromhex('...')])",
    },
    {
        "title": "Bitta Baytli XOR",
        "description": """Noma'lum bitta baytli kalit bilan shifrlangan. Kalitni toping va deshifrlang!
<code>2b 0e 0b 0b 5c 79 76 6d 6f 76 5c 78 7c 79 55 7c 76</code>
Maslahat: flag har doim NULL{ bilan boshlanadi.""",
        "category": "XOR",
        "difficulty": "o'rta",
        "points": 175,
        "flag": "NULL{single_byte_xor}",
        "hint": "N ^ kalit = birinchi shifrlangan bayt. Demak kalit = N ^ birinchi_bayt",
    },
    {
        "title": "Ko'p Baytli XOR",
        "description": """Bu safar kalit bir necha baytdan iborat. Quyidagi hex ni deshifrlang:
Kalit: <code>SECRET</code> (ASCII)
<code>9d c4 c5 c1 7e 84 95 c1 84 95 9c 84 9c 84 8d 94 9c</code>""",
        "category": "XOR",
        "difficulty": "qiyin",
        "points": 250,
        "flag": "NULL{multi_byte_xor_key}",
        "hint": "Kalit takrorlanadi: SECRETSECRETSECRET...",
    },
    {
        "title": "XOR Frekvens Tahlil",
        "description": """Uzun matn noma'lum kalit bilan XOR qilingan. Ingliz tilidagi eng ko'p uchraydigan harf 'e' (ASCII 101). Kalitni aniqlang:
<code>Fayl: <a href='/static/files/xor_freq.bin' download>xor_freq.bin</a></code>
(Masala maqsadida: kalit 0x73)""",
        "category": "XOR",
        "difficulty": "qiyin",
        "points": 300,
        "flag": "NULL{frequency_analysis_wins}",
        "hint": "Eng ko'p uchraydigan bayt 0x73 ^ 0x20 = 0x53 = 'S'... Yo'q, eng ko'p = 'e'=0x65",
    },

    # ══════════════════════════════════════════════
    # VIGENERE KATEGORIYASI
    # ══════════════════════════════════════════════
    {
        "title": "Vigenere Asoslari",
        "description": """Vigenère shifri Caesar shifrining kuchaytrilgan ko'rinishi.
Kalit: <code>KEY</code>
Shifrlangan: <code>XYMM{zkqztkxt_oy_zsxzout}</code>""",
        "category": "Vigenere",
        "difficulty": "o'rta",
        "points": 175,
        "flag": "NULL{vigenere_is_polyion}",
        "hint": "Har harfni kalit harfi siljishi bilan orqaga suring: K=10, E=4, Y=24",
    },
    {
        "title": "Kasiski Testi",
        "description": """Vigenère shifrini sinish usuli - Kasiski testi. Takrorlanuvchi ketma-ketliklarni toping va kalit uzunligini aniqlang:
<code>LXFOPVEFRNHR</code>
Kalit so'zi: <code>CRYPTO</code> (faqat tekshirish uchun)""",
        "category": "Vigenere",
        "difficulty": "qiyin",
        "points": 300,
        "flag": "NULL{kasiski_test_works}",
        "hint": "Takrorlanuvchi 3-gram larni toping, GCD hisoblang",
    },

    # ══════════════════════════════════════════════
    # HASHING KATEGORIYASI
    # ══════════════════════════════════════════════
    {
        "title": "MD5 Cracking",
        "description": """Bu MD5 hashni cracking qiling (rainbow table yoki brute force):
<code>5f4dcc3b5aa765d61d8327deb882cf99</code>
Oddiy so'z.""",
        "category": "Hashing",
        "difficulty": "oson",
        "points": 100,
        "flag": "NULL{password}",
        "hint": "crackstation.net yoki hashcat dan foydalaning",
    },
    {
        "title": "SHA1 Topishmoq",
        "description": """SHA1 hashni toping va deshifrlang:
<code>da39a3ee5e6b4b0d3255bfef95601890afd80709</code>
Bu nima?""",
        "category": "Hashing",
        "difficulty": "oson",
        "points": 75,
        "flag": "NULL{empty_string}",
        "hint": "Bo'sh satrning SHA1 hashi",
    },
    {
        "title": "Hash Zanjiri",
        "description": """Ketma-ket hashni deshifrlang:
1. MD5("raqam") → hash1
2. SHA256(hash1) → <code>6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b</code>
"raqam" nima?""",
        "category": "Hashing",
        "difficulty": "o'rta",
        "points": 200,
        "flag": "NULL{1}",
        "hint": "SHA256('1' ning MD5 hashi) - raqam 1 dan 9 gacha",
    },
    {
        "title": "Bcrypt Parol",
        "description": """Bcrypt hash - zamonaviy parol saqlash:
<code>$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW</code>
Ushbu bcrypt hashga mos parol: oddiy ingliz so'zi.""",
        "category": "Hashing",
        "difficulty": "qiyin",
        "points": 350,
        "flag": "NULL{secret}",
        "hint": "hashcat -m 3200 bilan wordlist ishlatib ko'ring",
    },

    # ══════════════════════════════════════════════
    # RSA KATEGORIYASI
    # ══════════════════════════════════════════════
    {
        "title": "RSA - Kichik e",
        "description": """RSA parametrlari berilgan. Deshifrlang:
<code>
n = 3233
e = 17
c = 2790
</code>
p va q ni toping, d ni hisoblang, deshifrlang.""",
        "category": "RSA",
        "difficulty": "o'rta",
        "points": 250,
        "flag": "NULL{65}",
        "hint": "n = p*q → n = 61*53. phi = (p-1)*(q-1). d = modinverse(e, phi)",
    },
    {
        "title": "RSA - Umumiy modul",
        "description": """Ikkita xabar bir xil n bilan shifrlangan, lekin turli e bilan. Bu common modulus hujumi!
<code>
n = 17984577571991
e1 = 65537, c1 = 12345678901234
e2 = 65539, c2 = 98765432109876
</code>""",
        "category": "RSA",
        "difficulty": "qiyin",
        "points": 400,
        "flag": "NULL{common_modulus}",
        "hint": "gcd(e1, e2) = 1 bo'lsa, Extended Euclidean Algorithm ishlatiladi",
    },
    {
        "title": "RSA - Kichik n",
        "description": """n juda kichik, faktorizatsiya qiling:
<code>
n = 2867
e = 3
c = 2769
</code>""",
        "category": "RSA",
        "difficulty": "o'rta",
        "points": 200,
        "flag": "NULL{97}",
        "hint": "n ni p va q ga faktorizatsiya qiling: sqrt(n) atrofida qidiring",
    },
    {
        "title": "RSA - Wiener Hujumi",
        "description": """d juda kichik bo'lganda Wiener hujumi ishlaydi:
<code>
n = 90581
e = 17993
</code>
d ni toping (Wiener's algorithm)""",
        "category": "RSA",
        "difficulty": "qiyin",
        "points": 500,
        "flag": "NULL{5}",
        "hint": "d < n^0.25 bo'lsa Wiener ishlaydi. Continued fractions ishlatiladi.",
    },
    {
        "title": "RSA - e=3 Cube Root",
        "description": """e=3 va m juda kichik bo'lsa, oddiy kub ildiz olish yetarli:
<code>
n = (katta son)
e = 3
c = 125
</code>
m = ?""",
        "category": "RSA",
        "difficulty": "o'rta",
        "points": 225,
        "flag": "NULL{5}",
        "hint": "Agar m^3 < n bo'lsa, c^(1/3) = m",
    },

    # ══════════════════════════════════════════════
    # AES KATEGORIYASI
    # ══════════════════════════════════════════════
    {
        "title": "AES-ECB Penguen",
        "description": """AES-ECB rejimi xavfli - bir xil bloklar bir xil chiqqani uchun naqsh ko'rinadi.
Ushbu ECB shifrlangan faylni deshifrlang:
Kalit: <code>YELLOW SUBMARINE</code>
<code>636f6f6b626f6f6b7b6563625f70656e67756e7d</code>
(Bu oddiy misol, asl fayl uchun hint ko'ring)""",
        "category": "AES",
        "difficulty": "o'rta",
        "points": 250,
        "flag": "NULL{ecb_penguin}",
        "hint": "from Crypto.Cipher import AES; cipher = AES.new(key, AES.MODE_ECB)",
    },
    {
        "title": "AES-CBC Padding Oracle",
        "description": """CBC rejimida padding oracle hujumi. Server sizga padding to'g'ri yoki noto'g'ri ekanini aytadi.
Bu kontseptual masala:
Tekshirilgan ciphertext: <code>NULL{padding_oracle_ftw}</code>
(To'liq hujumni tushunish uchun academy bo'limiga qarang)""",
        "category": "AES",
        "difficulty": "qiyin",
        "points": 500,
        "flag": "NULL{padding_oracle_ftw}",
        "hint": "IV va C1 blokini manipulyatsiya qiling, padding xatosiga e'tibor bering",
    },
    {
        "title": "AES-CTR Reuse",
        "description": """CTR rejimida bir xil nonce ikki marta ishlatilgan!
<code>
ct1 = 1a2b3c4d5e (hex)
ct2 = 1a2b3c5548 (hex)
pt1 = "hello"
</code>
pt2 nima?""",
        "category": "AES",
        "difficulty": "qiyin",
        "points": 400,
        "flag": "NULL{nonce}",
        "hint": "XOR xususiyati: ct1 XOR ct2 = pt1 XOR pt2",
    },

    # ══════════════════════════════════════════════
    # STEGANOGRAFIYA
    # ══════════════════════════════════════════════
    {
        "title": "LSB Steganografiya",
        "description": """Rasmda yashiringan xabar bor. Har bir pikselning eng kam ahamiyatli biti (LSB) ni o'qing.
<code>Hint: flag NULL{ bilan boshlanadi. 
Bu masalada pixel qiymatlari: [78, 85, 76, 76, 123, 108, 115, 98, 125]</code>
(Har bir qiymat to'g'ridan to'g'ri ASCII)""",
        "category": "Steganography",
        "difficulty": "o'rta",
        "points": 200,
        "flag": "NULL{lsb}",
        "hint": "Python PIL/Pillow kutubxonasini ishlatib piksellarni o'qing",
    },
    {
        "title": "Strings da Yashiringan",
        "description": """Ba'zan flag oddiy matnda yashiringan bo'ladi. Linux 'strings' buyrug'i yordamida:
<code>Bu matning ichida NULL{strings_command} yashiringan. Uni toping!</code>""",
        "category": "Steganography",
        "difficulty": "oson",
        "points": 50,
        "flag": "NULL{strings_command}",
        "hint": "strings filename | grep NULL",
    },

    # ══════════════════════════════════════════════
    # MATEMATIK / NUMBER THEORY
    # ══════════════════════════════════════════════
    {
        "title": "Modular Arifmetika",
        "description": """Kriptografiyaning asosi - modular arifmetika.
Hisoblang: <code>7^365 mod 13</code>
Javobni NULL{javob} formatida yuboring.""",
        "category": "Math",
        "difficulty": "oson",
        "points": 100,
        "flag": "NULL{1}",
        "hint": "Python: pow(7, 365, 13) - tez darajaga ko'tarish",
    },
    {
        "title": "Extended Euclidean",
        "description": """gcd(a, b) = a*x + b*y
<code>gcd(35, 15) = ?
x = ?, y = ?</code>
NULL{gcd_x_y} formatida yuboring (masalan NULL{5_1_-2})""",
        "category": "Math",
        "difficulty": "o'rta",
        "points": 150,
        "flag": "NULL{5_1_-2}",
        "hint": "gcd(35,15): 35 = 2*15 + 5, 15 = 3*5 + 0",
    },
    {
        "title": "Discrete Logarithm",
        "description": """Diffie-Hellman asosi - diskret logarifm.
<code>g = 5, p = 23, g^x mod p = 8</code>
x = ? (brute force ishlaydi, p kichik)""",
        "category": "Math",
        "difficulty": "o'rta",
        "points": 200,
        "flag": "NULL{6}",
        "hint": "5^x mod 23 = 8 → x ni 1 dan 22 gacha sinab ko'ring",
    },
    {
        "title": "CRT (Xitoy Qoldig'i Teoremasi)",
        "description": """Xitoy Qoldig'i Teoremasi RSA da ishlatiladi.
<code>
x ≡ 2 (mod 3)
x ≡ 3 (mod 5)
x ≡ 2 (mod 7)
</code>
x = ? (eng kichik musbat son)""",
        "category": "Math",
        "difficulty": "o'rta",
        "points": 225,
        "flag": "NULL{23}",
        "hint": "CRT: x = Σ(ai * Mi * yi) mod M, bu yerda M = 3*5*7 = 105",
    },

    # ══════════════════════════════════════════════
    # DIFFIE-HELLMAN
    # ══════════════════════════════════════════════
    {
        "title": "DH Kalit Almashish",
        "description": """Diffie-Hellman kalit almashish protokoli.
<code>
p = 23, g = 5
Alice: a = 6, A = g^a mod p = ?
Bob: b = 15, B = g^b mod p = ?
Umumiy kalit K = ?
</code>""",
        "category": "DH",
        "difficulty": "o'rta",
        "points": 200,
        "flag": "NULL{2}",
        "hint": "A = 5^6 mod 23 = 8, B = 5^15 mod 23 = 19, K = 8^15 mod 23 = B^a mod p",
    },

    # ══════════════════════════════════════════════
    # MISC / ARALASH
    # ══════════════════════════════════════════════
    {
        "title": "QR Kod",
        "description": """Flagni QR koddan o'qing:
Bu vazifada QR kod qiymati baza64 da berilgan - uni rasm faylga aylantiring va skanerlang.
<code>Flag: NULL{qr_c0d3s_ar3_fun}</code> (To'g'ridan to'g'ri)""",
        "category": "Misc",
        "difficulty": "oson",
        "points": 75,
        "flag": "NULL{qr_c0d3s_ar3_fun}",
        "hint": "zbarimg yoki online QR scanner ishlatib ko'ring",
    },
    {
        "title": "JWT Token",
        "description": """Bu JWT tokenni tahlil qiling:
<code>eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4iLCJmbGFnIjoiTlVMTHtqd3Rfbm9uZV9hbGd9In0.</code>
Flagni toping.""",
        "category": "Misc",
        "difficulty": "o'rta",
        "points": 175,
        "flag": "NULL{jwt_none_alg}",
        "hint": "JWT = header.payload.signature, har biri base64. Payload ni decode qiling.",
    },
    {
        "title": "SQL Injection Login Bypass",
        "description": """Login formada SQL injection orqali admin sifatida kiring:
Username: <code>admin'--</code>
Password: (istalgan narsa)
<br><br>Ushbu kontseptual masalada flag: NULL{sql_inj3ct10n}""",
        "category": "Web",
        "difficulty": "o'rta",
        "points": 150,
        "flag": "NULL{sql_inj3ct10n}",
        "hint": "SQL: SELECT * FROM users WHERE user='' OR 1=1--' AND pass=''",
    },
    {
        "title": "Fermat Faktorizatsiya",
        "description": """p va q bir biriga yaqin bo'lsa, Fermat faktorizatsiyasi tez ishlaydi:
<code>n = 100000007</code>
p va q ni toping, kichig'ini flag sifatida yuboring: NULL{kichiq_son}""",
        "category": "RSA",
        "difficulty": "qiyin",
        "points": 350,
        "flag": "NULL{9999}",
        "hint": "a = ceil(sqrt(n)), b2 = a^2 - n, agar b to'liq kvadrat bo'lsa p = a-b, q = a+b",
    },
    {
        "title": "OTP (One Time Pad)",
        "description": """Teoriyada buzib bo'lmaydigan shifr - lekin bir marta ishlatilishi kerak!
<code>
pt1 = "attack at dawn"
ct1 = 0x45bfa9...
ct2 = 0x41b8ac...  (bir xil kalit ishlatilgan!)
</code>
pt2 ni toping: NULL{pt2}
(Bu masalada pt2 = "NULL{reused_otp}")""",
        "category": "XOR",
        "difficulty": "qiyin",
        "points": 400,
        "flag": "NULL{reused_otp}",
        "hint": "ct1 XOR ct2 = pt1 XOR pt2, demak pt2 = (ct1 XOR ct2) XOR pt1",
    },
    {
        "title": "Pohlig-Hellman",
        "description": """p-1 ning barcha omillari kichik bo'lsa (smooth), diskret logarifmni tez hisoblash mumkin.
<code>g=2, p=29, g^x mod p = 17</code>
x = ?""",
        "category": "Math",
        "difficulty": "qiyin",
        "points": 450,
        "flag": "NULL{12}",
        "hint": "p-1 = 28 = 4*7. Pohlig-Hellman: x mod 4, x mod 7 toping, CRT bilan birlashtiring",
    },
    {
        "title": "Baby-Step Giant-Step",
        "description": """Diskret logarifmni O(sqrt(n)) da hisoblash:
<code>g = 2, p = 113, h = 57</code>
x = g^? mod p = h""",
        "category": "Math",
        "difficulty": "qiyin",
        "points": 400,
        "flag": "NULL{36}",
        "hint": "m = ceil(sqrt(p)). Baby steps: {j: g^j mod p}. Giant steps: h*(g^-m)^i",
    },
    {
        "title": "Playfair Shifri",
        "description": """Playfair shifri 5x5 matritsa ishlatadi, digraflarni shifrlaydi.
Kalit: <code>MONARCHY</code>
Shifrlangan: <code>CFHGCE</code>
Deshifrlang!""",
        "category": "Classical",
        "difficulty": "qiyin",
        "points": 350,
        "flag": "NULL{BALLAD}",
        "hint": "Playfair: bir xil qatorda → chap; bir xil ustunda → yuqori; boshqa → to'rtburchak",
    },
    {
        "title": "Hill Shifri",
        "description": """Hill shifri matritsali ko'paytirish ishlatadi.
<code>
Kalit matritsa: [[6,24],[1,13]] mod 26
Shifrlangan: POHL
</code>
Deshifrlang: NULL{...}""",
        "category": "Classical",
        "difficulty": "qiyin",
        "points": 400,
        "flag": "NULL{HELP}",
        "hint": "Kalit matritsasining modular teskari matritsasini toping",
    },
    {
        "title": "Double Transposition",
        "description": """Ikki marta ko'chirish shifri.
<code>
Birinchi kalit: 3142 (ustunlar tartibi)
Ikkinchi kalit: 2413
Shifrlangan: LNULT}N{L
</code>""",
        "category": "Classical",
        "difficulty": "qiyin",
        "points": 350,
        "flag": "NULL{NULL}",
        "hint": "Avval ikkinchi transpositionni teskari qiling, keyin birinchisini",
    },
    {
        "title": "LFSR (Linear Feedback Shift Register)",
        "description": """LFSR - hardware random number generator.
<code>
LFSR uzunligi: 4 bit
Boshlang'ich holat: [1,0,1,1]
Taps: [4,3]
Birinchi 8 ta chiqish: 1,1,0,1,...
To'liq davr: ?
</code>
NULL{davriy_son}""",
        "category": "Stream",
        "difficulty": "qiyin",
        "points": 450,
        "flag": "NULL{15}",
        "hint": "4-bit LFSR maksimal davri 2^4 - 1 = 15 bo'lishi mumkin",
    },
    {
        "title": "Salsa20 Nonce",
        "description": """Salsa20 stream cipher - nonce bir marta ishlatilishi kerak!
<code>
ct1 hex: a3 b2 c1
ct2 hex: a3 b2 d4  (bir xil kalit va nonce!)
pt1: "abc"
pt2 = ?
</code>""",
        "category": "Stream",
        "difficulty": "qiyin",
        "points": 400,
        "flag": "NULL{abd}",
        "hint": "Stream cipher: XOR bilan shifrlaydi. ct1 XOR ct2 = pt1 XOR pt2",
    },
    {
        "title": "Enigma Machine",
        "description": """WWII mashhur shifrlash mashinasi.
<code>
Rotor I, II, III (chapdan o'ngga)
Reflektor B
Ring setting: AAA
Kalit holati: AAA
Shifrlangan: BDZGO (5 ta harf)
</code>
Deshifrlang!""",
        "category": "Classical",
        "difficulty": "qiyin",
        "points": 500,
        "flag": "NULL{HELLO}",
        "hint": "Online Enigma simulyatoridan foydalaning yoki py-enigma kutubxonasi",
    },
    {
        "title": "Substitution Cipher (Frequency)",
        "description": """Oddiy almashtirish shifri - frekvens tahlil bilan buzing!
<code>
GJUUT YTNZY OZ OCZ GJUZ GJUUT NZXGZO
(Ko'p uchraydigan harf: G=L, Z=E, T=O)
</code>""",
        "category": "Classical",
        "difficulty": "o'rta",
        "points": 275,
        "flag": "NULL{LOLLY}",
        "hint": "Ingliz tilida eng ko'p: E, T, A, O, I. Qisqa so'zlar: THE, AND, IS",
    },
    {
        "title": "Railfence Cipher",
        "description": """Temir yo'l to'siq shifri - matn zigzag usulida yoziladi.
<code>
Rails (qatorlar): 3
Shifrlangan: WECRLTEERDSOEEFEAABORADICVNE
</code>
Deshifrlang!""",
        "category": "Transposition",
        "difficulty": "o'rta",
        "points": 200,
        "flag": "NULL{WEAREDISCOVEREDFLEEAONCE}",
        "hint": "3 rail: yuqori, o'rta, quyi - zigzag naqshi",
    },
    {
        "title": "Pollard Rho",
        "description": """Pollard's ρ algoritmi - kichikroq n uchun faktorizatsiya:
<code>n = 8051</code>
p va q ni toping, NULL{p*q bu yerda p < q} kichig'ini yuboring""",
        "category": "RSA",
        "difficulty": "qiyin",
        "points": 450,
        "flag": "NULL{83}",
        "hint": "Pollard rho: x = x^2 + c mod n, gcd(|x-y|, n). n = 83 * 97",
    },
    {
        "title": "El Gamal Shifri",
        "description": """El Gamal asimmetrik shifr:
<code>
p = 23, g = 5
Bob's private key: x = 6 → y = g^x mod p = 8
Alice yuboradi: (c1, c2) = (18, 6)
</code>
Deshifrlang: m = c2 * (c1^x)^-1 mod p""",
        "category": "Asymmetric",
        "difficulty": "qiyin",
        "points": 400,
        "flag": "NULL{10}",
        "hint": "s = c1^x mod p = 18^6 mod 23. m = c2 * s^-1 mod 23",
    },
    {
        "title": "Blind SQL to'liq",
        "description": """Boolean-based blind SQL injection. Har bir so'rov True/False qaytaradi.
<code>
URL: /user?id=1
True: sahifa ko'rinadi
False: 'User not found'
Flag birinchi belgisi: ORD(SUBSTRING(flag,1,1))=78 → True (N=78)
</code>
Flagni belgima-belgi toping: NULL{blind_sqli}""",
        "category": "Web",
        "difficulty": "qiyin",
        "points": 500,
        "flag": "NULL{blind_sqli}",
        "hint": "Binary search: ASCII 32-127 oralig'ida ikkilik qidiruv",
    },
    {
        "title": "HMAC Forgery",
        "description": """Length Extension hujumi - MD5 va SHA1 ga qarshi:
<code>
HMAC-MD5(secret || "admin=false") bilasiz
secret uzunligi = 10 bayt
</code>
"admin=true" uchun HMAC yasang.
(Kontseptual: NULL{length_extension_attack})""",
        "category": "Hashing",
        "difficulty": "qiyin",
        "points": 500,
        "flag": "NULL{length_extension_attack}",
        "hint": "hashpump yoki hlextend vositasini ishlatib ko'ring",
    },
]
