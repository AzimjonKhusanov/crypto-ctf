# ── NullCTF Dockerfile ─────────────────────────────────────────────────────
FROM python:3.11-slim

LABEL maintainer="NullCTF"
LABEL description="O'zbek tilida kriptografiya CTF platformasi"

# Ish papkasi
WORKDIR /app

# Tizim paketlari
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Python kutubxonalari
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Loyiha fayllarini ko'chirish
COPY . .

# Ma'lumotlar bazasi uchun papka
RUN mkdir -p /app/data

# Statik fayllar va shablonlar uchun ruxsat
RUN chmod -R 755 /app/frontend

# Port ochish
EXPOSE 5000

# Muhit o'zgaruvchilari (prod da o'zgartiring!)
ENV FLASK_ENV=production
ENV SECRET_KEY=change-this-in-production-use-strong-random-key
ENV DATABASE_URL=sqlite:////app/data/nullctf.db
ENV ADMIN_USERNAME=admin

# Ishga tushirish
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "60", "run:app"]
