"""
Ma'lumotlar bazasi modellari
"""

import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


# ═══════════════════════════════════════════════════════════════════════════════
# Foydalanuvchi modeli
# ═══════════════════════════════════════════════════════════════════════════════
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(50), unique=True, nullable=False)
    email         = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    score         = db.Column(db.Integer, default=0)
    is_admin      = db.Column(db.Boolean, default=False)
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)

    submissions = db.relationship('Submission', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def solved_challenges(self):
        return [s.challenge_id for s in self.submissions.filter_by(correct=True)]

    def __repr__(self):
        return f'<User {self.username}>'


# ═══════════════════════════════════════════════════════════════════════════════
# Challenge modeli
# ═══════════════════════════════════════════════════════════════════════════════
class Challenge(db.Model):
    __tablename__ = 'challenges'

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category    = db.Column(db.String(50), nullable=False)   # RSA, XOR, AES, ...
    difficulty  = db.Column(db.String(20), nullable=False)   # oson, o'rta, qiyin
    points      = db.Column(db.Integer, default=100)
    flag        = db.Column(db.String(300), nullable=False)  # NULL{...}
    hint        = db.Column(db.Text)
    attachment  = db.Column(db.String(300))                  # fayl yo'li (ixtiyoriy)
    is_active   = db.Column(db.Boolean, default=True)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    submissions = db.relationship('Submission', backref='challenge', lazy='dynamic')
    writeups    = db.relationship('Writeup', backref='challenge', lazy='dynamic')

    def solve_count(self):
        return self.submissions.filter_by(correct=True).count()

    def __repr__(self):
        return f'<Challenge {self.title}>'


# ═══════════════════════════════════════════════════════════════════════════════
# Submission (topshiriq) modeli
# ═══════════════════════════════════════════════════════════════════════════════
class Submission(db.Model):
    __tablename__ = 'submissions'

    id           = db.Column(db.Integer, primary_key=True)
    user_id      = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenges.id'), nullable=False)
    flag_attempt = db.Column(db.String(300), nullable=False)
    correct      = db.Column(db.Boolean, default=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Submission {self.user_id} -> {self.challenge_id} [{self.correct}]>'


# ═══════════════════════════════════════════════════════════════════════════════
# Academy darslari
# ═══════════════════════════════════════════════════════════════════════════════
class Lesson(db.Model):
    __tablename__ = 'lessons'

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(200), nullable=False)
    slug        = db.Column(db.String(200), unique=True, nullable=False)
    category    = db.Column(db.String(50), nullable=False)
    order_num   = db.Column(db.Integer, default=0)
    content     = db.Column(db.Text, nullable=False)   # Markdown/HTML
    difficulty  = db.Column(db.String(20), default='oson')
    is_active   = db.Column(db.Boolean, default=True)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Lesson {self.title}>'


# ═══════════════════════════════════════════════════════════════════════════════
# Writeup modeli
# ═══════════════════════════════════════════════════════════════════════════════
class Writeup(db.Model):
    __tablename__ = 'writeups'

    id           = db.Column(db.Integer, primary_key=True)
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenges.id'), nullable=False)
    title        = db.Column(db.String(200), nullable=False)
    content      = db.Column(db.Text, nullable=False)  # Markdown
    author       = db.Column(db.String(100), default='Admin')
    is_active    = db.Column(db.Boolean, default=True)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Writeup {self.title}>'


# ═══════════════════════════════════════════════════════════════════════════════
# Ma'lumotlarni to'ldirish (seed)
# ═══════════════════════════════════════════════════════════════════════════════
def init_db(app):
    """Boshlang'ich ma'lumotlarni bazaga yuklash"""
    from .seed_challenges import CHALLENGES
    from .seed_lessons import LESSONS
    from .seed_writeups import WRITEUPS
    import bcrypt

    # Admin foydalanuvchisini yaratish
    admin_username = app.config.get('ADMIN_USERNAME', 'admin')
    admin_pw_hash  = app.config.get('ADMIN_PASSWORD_HASH', '')

    if not User.query.filter_by(username=admin_username).first():
        admin = User(
            username   = admin_username,
            email      = 'admin@nullctf.uz',
            is_admin   = True,
            score      = 0,
        )
        # Agar env da hash bo'lsa uni ishlatamiz, aks holda default
        if admin_pw_hash:
            admin.password_hash = admin_pw_hash
        else:
            admin.set_password('Admin@NullCTF2024!')
        db.session.add(admin)
        db.session.commit()
        print('[*] Admin yaratildi.')

    # Challengelarni yuklash
    if Challenge.query.count() == 0:
        for ch in CHALLENGES:
            challenge = Challenge(**ch)
            db.session.add(challenge)
        db.session.commit()
        print(f'[*] {len(CHALLENGES)} ta challenge yuklandi.')

    # Darslarni yuklash
    if Lesson.query.count() == 0:
        for ls in LESSONS:
            lesson = Lesson(**ls)
            db.session.add(lesson)
        db.session.commit()
        print(f'[*] {len(LESSONS)} ta dars yuklandi.')

    # Writeuplarni yuklash
    if Writeup.query.count() == 0:
        for wu in WRITEUPS:
            chall = Challenge.query.filter_by(title=wu['challenge_title']).first()
            if chall:
                writeup = Writeup(
                    challenge_id=chall.id,
                    title=wu['title'],
                    content=wu['content'],
                    author=wu.get('author', 'NullCTF Team'),
                )
                db.session.add(writeup)
        db.session.commit()
        print('[*] Writeuplar yuklandi.')
