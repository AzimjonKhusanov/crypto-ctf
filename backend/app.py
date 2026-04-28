"""
NullCTF - O'zbek tilida kriptografiya CTF platformasi
Asosiy Flask ilovasi
"""

import os
import sys
from flask import Flask
from flask_login import LoginManager
from .models.database import db, init_db
from .routes.auth import auth_bp
from .routes.challenges import challenges_bp
from .routes.academy import academy_bp
from .routes.writeups import writeups_bp
from .routes.admin import admin_bp
from .routes.api import api_bp


def create_app(config=None):
    app = Flask(
        __name__,
        template_folder='../frontend/templates',
        static_folder='../frontend/static'
    )

    # ── Konfiguratsiya ──────────────────────────────────────────────────────
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-in-prod')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', 'sqlite:///nullctf.db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ADMIN_USERNAME'] = os.environ.get('ADMIN_USERNAME', 'admin')
    app.config['ADMIN_PASSWORD_HASH'] = os.environ.get('ADMIN_PASSWORD_HASH', '')

    if config:
        app.config.update(config)

    # ── Bazani ulash ────────────────────────────────────────────────────────
    db.init_app(app)

    # ── Login manager ───────────────────────────────────────────────────────
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Iltimos, tizimga kiring.'

    from .models.database import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # ── Blueprintlar ────────────────────────────────────────────────────────
    app.register_blueprint(auth_bp)
    app.register_blueprint(challenges_bp)
    app.register_blueprint(academy_bp)
    app.register_blueprint(writeups_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    # ── Bazani yaratish va seed data qo'shish ───────────────────────────────
    with app.app_context():
    	from sqlalchemy import inspect

    	inspector = inspect(db.engine)

    # Agar users table yo‘q bo‘lsa — yaratamiz
    	if not inspector.has_table("users"):
        	db.create_all()
        	init_db(app)

    return app
