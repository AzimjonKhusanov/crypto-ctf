# 🔐 NullCTF — O'zbek Kriptografiya CTF Platformasi

```
 _   _       _ _  ____ _____ _____
| \ | |_   _| | |/ ___|_   _|  ___|
|  \| | | | | | | |     | | | |_
| |\  | |_| | | | |___  | | |  _|
|_| \_|\__,_|_|_|\____| |_| |_|

NULL{flag_seni_kutmoqda}
```

O'zbek tilida to'liq kriptografiya CTF platformasi. Challengelar, Academy darslari,
Writeuplar va Admin panel.

---

## 🚀 Tezkor Ishga Tushirish

### 1. Docker bilan (tavsiya etiladi)

```bash
# 1. Loyihani klonlash
git clone https://github.com/yourname/nullctf.git
cd nullctf

# 2. .env fayl yaratish
cp .env.example .env
# .env faylni o'zingizga moslang (SECRET_KEY va admin sozlamalari)

# 3. Ishga tushirish — bitta buyruq!
docker-compose up -d

# Platforma: http://localhost:5000
```

### 2. Python bilan (local dev)

```bash
# 1. Virtual muhit
python3 -m venv venv
source venv/bin/activate       # Linux/Mac
# venv\Scripts\activate        # Windows

# 2. Kutubxonalarni o'rnatish
pip install -r requirements.txt

# 3. Muhit o'zgaruvchilari
cp .env.example .env
export SECRET_KEY="dev-secret"
export ADMIN_USERNAME="admin"

# 4. Ishga tushirish
python run.py

# Platforma: http://localhost:5000
```

---

## 🔑 Admin Paroli O'rnatish

Admin paroli environment variable orqali o'rnatiladi (xavfsizlik uchun):

```bash
# Bcrypt hash yaratish
python3 -c "
from werkzeug.security import generate_password_hash
parol = 'SizningKuchlParolingiz123!'
print(generate_password_hash(parol))
"

# Natijani .env ga yozing:
# ADMIN_PASSWORD_HASH=pbkdf2:sha256:...

# Yoki docker-compose.yml da:
# - ADMIN_PASSWORD_HASH=pbkdf2:sha256:...
```

> **Muhim:** Agar `ADMIN_PASSWORD_HASH` o'rnatilmasa, default parol ishlatiladi:
> `Admin@NullCTF2024!` — **ishlab chiqarishda albatta o'zgartiring!**

---

## 📁 Loyiha Strukturasi

```
nullctf/
├── run.py                      # Ishga tushirish nuqtasi
├── requirements.txt            # Python kutubxonalari
├── Dockerfile                  # Docker image
├── docker-compose.yml          # Docker Compose
├── .env.example                # Muhit o'zgaruvchilari namunasi
│
├── backend/                    # Backend (Flask)
│   ├── app.py                  # Flask ilovasi factory
│   ├── models/
│   │   ├── database.py         # SQLAlchemy modellari
│   │   ├── seed_challenges.py  # 50+ ta challenge
│   │   ├── seed_lessons.py     # 10 ta Academy darsi
│   │   └── seed_writeups.py    # Writeup namunalari
│   └── routes/
│       ├── auth.py             # Kirish/chiqish/profil
│       ├── challenges.py       # Challengelar + flag topshirish
│       ├── academy.py          # Darslar
│       ├── writeups.py         # Writeuplar
│       ├── admin.py            # Admin panel
│       └── api.py              # REST API
│
└── frontend/                   # Frontend
    ├── static/
    │   ├── css/main.css        # Dark CTF uslub
    │   └── js/main.js          # Interaktivlik
    └── templates/
        ├── base.html           # Asosiy shablon
        ├── index.html          # Bosh sahifa
        ├── auth/               # Login, Register, Profile
        ├── challenges/         # Challengelar ro'yxati, detail, scoreboard
        ├── academy/            # Darslar
        ├── writeups/           # Writeuplar
        └── admin/              # Admin panel
```

---

## 🌐 Asosiy Sahifalar

| URL | Tavsif |
|-----|--------|
| `/` | Bosh sahifa |
| `/challenges` | Barcha challengelar |
| `/challenges/<id>` | Challenge detail + flag topshirish |
| `/academy` | Darslar ro'yxati |
| `/academy/<slug>` | Dars detail |
| `/writeups` | Writeuplar |
| `/writeups/<id>` | Writeup detail |
| `/scoreboard` | Ball jadvali |
| `/profile` | Shaxsiy profil |
| `/admin` | Admin panel |
| `/api/challenges` | API — challengelar |
| `/api/scoreboard` | API — scoreboard |
| `/api/stats` | API — statistika |
| `/api/submit` | API — flag topshirish (POST) |

---

## 📚 Academy Darslari

1. **Kriptografiyaga Kirish** — Asosiy tushunchalar
2. **Base64 Encoding** — Encoding/decoding
3. **XOR Operatsiyasi** — XOR va kriptografiya
4. **Caesar Shifri** — Klassik siljish shifri
5. **Vigenère Shifri** — Polialfabetik shifr
6. **RSA Kriptografiyasi** — Asimmetrik shifrlash
7. **AES Shifri** — Zamonaviy simmetrik shifr
8. **Hash Funksiyalari** — MD5, SHA256, bcrypt
9. **Diffie-Hellman** — Kalit almashish protokoli
10. **Modular Arifmetika** — Kriptografiya matematikasi

---

## 🏆 Challenge Kategoriyalari

| Kategoriya | Ta'rif | Misol |
|-----------|---------|-------|
| **Encoding** | Ma'lumot kodlash | Base64, Hex, Binary |
| **Caesar** | Klassik siljish shifri | ROT13, ROT47 |
| **XOR** | Eksklyuziv OR operatsiyasi | Single/Multi byte XOR |
| **Vigenere** | Polialfabetik shifr | Kasiski testi |
| **Hashing** | Hash funksiyalar | MD5, SHA1, bcrypt |
| **RSA** | Asimmetrik kriptografiya | Faktorizatsiya, Wiener |
| **AES** | Simmetrik blok shifr | ECB, CBC, CTR |
| **Classical** | Klassik shifrlar | Playfair, Hill, Enigma |
| **Math** | Raqamlar nazariyasi | CRT, DLOG, Fermat |
| **DH** | Diffie-Hellman | Kalit almashish |
| **Stream** | Stream shifrlar | LFSR, Salsa20 |
| **Steganography** | Yashirin xabarlar | LSB, Strings |
| **Web** | Veb xavfsizlik | SQLi, JWT |
| **Misc** | Boshqalar | QR, Morse |

---

## 🔒 Xavfsizlik

- **Parollar** — bcrypt orqali hash qilingan
- **Session** — Flask-Login bilan himoyalangan
- **Admin** — Alohida rol tekshiruvi
- **SQL Injection** — SQLAlchemy ORM xavfsiz
- **Environment** — Barcha sirlar env orqali

---

## 🛠️ Yangi Challenge Qo'shish

### Admin panel orqali:
1. `/admin/challenges/new` ga kiring
2. Formani to'ldiring
3. Flag formatiga rioya qiling: `NULL{...}`

### Kod orqali (`seed_challenges.py`):
```python
{
    "title": "Yangi Masala",
    "description": "Masala tavsifi...",
    "category": "RSA",
    "difficulty": "o'rta",   # oson | o'rta | qiyin
    "points": 200,
    "flag": "NULL{yangi_flag}",
    "hint": "Maslahat matni",
}
```

---

## 📊 API Endpointlar

```bash
# Barcha challengelar
curl http://localhost:5000/api/challenges

# Scoreboard
curl http://localhost:5000/api/scoreboard

# Statistika
curl http://localhost:5000/api/stats

# Flag topshirish (autentifikatsiya kerak)
curl -X POST http://localhost:5000/api/submit \
  -H "Content-Type: application/json" \
  -d '{"challenge_id": 1, "flag": "NULL{test}"}'
```

---

## 🐳 Docker Buyruqlari

```bash
# Ishga tushirish
docker-compose up -d

# Loglarni ko'rish
docker-compose logs -f

# To'xtatish
docker-compose down

# Yangilash (kod o'zgarsa)
docker-compose up -d --build

# Ma'lumotlar bazasini tozalash
docker-compose down -v
docker-compose up -d
```

---

## 📝 Muammo Bartaraf Etish

**Port band bo'lsa:**
```bash
# docker-compose.yml da portni o'zgartiring:
ports:
  - "8080:5000"   # 5000 o'rniga 8080
```

**Admin kirish ishlamasa:**
```bash
# Yangi hash yarating:
python3 -c "from werkzeug.security import generate_password_hash; print(generate_password_hash('YangParol'))"
# Natijani ADMIN_PASSWORD_HASH ga qo'ying
```

**Baza qayta yuklansin:**
```bash
rm nullctf.db   # yoki docker volume o'chiring
python run.py   # qayta ishga tushiring
```

---

## 🤝 Hissa Qo'shish

1. Yangi challenge yozing
2. Academy darslarini boyiting
3. Writeup qo'shing
4. Xatoliklarni bildiring

---

```
NULL{_muvaffaqiyatli_o'rnatildi_}
```
# crypto-ctf
# crypto-ctf
