"""
Autentifikatsiya yo'nalishlari — ro'yxatdan o'tish, kirish, chiqish
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from ..models.database import db, User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('challenges.index'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            flash(f'Xush kelibsiz, {user.username}!', 'success')
            return redirect(next_page or url_for('challenges.index'))
        else:
            flash('Foydalanuvchi nomi yoki parol noto\'g\'ri.', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('challenges.index'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email    = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm  = request.form.get('confirm_password', '')

        # Validatsiya
        if len(username) < 3:
            flash('Foydalanuvchi nomi kamida 3 ta belgidan iborat bo\'lishi kerak.', 'danger')
            return render_template('auth/register.html')

        if password != confirm:
            flash('Parollar mos kelmadi.', 'danger')
            return render_template('auth/register.html')

        if len(password) < 8:
            flash('Parol kamida 8 ta belgidan iborat bo\'lishi kerak.', 'danger')
            return render_template('auth/register.html')

        if User.query.filter_by(username=username).first():
            flash('Bu foydalanuvchi nomi band.', 'danger')
            return render_template('auth/register.html')

        if User.query.filter_by(email=email).first():
            flash('Bu email allaqachon ro\'yxatdan o\'tgan.', 'danger')
            return render_template('auth/register.html')

        # Yangi foydalanuvchi yaratish
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash('Muvaffaqiyatli ro\'yxatdan o\'tdingiz!', 'success')
        return redirect(url_for('challenges.index'))

    return render_template('auth/register.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Tizimdan chiqdingiz.', 'info')
    return redirect(url_for('auth.login'))


@auth_bp.route('/profile')
@login_required
def profile():
    solved = current_user.solved_challenges()
    from ..models.database import Challenge, Submission
    solved_challenges = Challenge.query.filter(Challenge.id.in_(solved)).all()
    recent_submissions = (Submission.query
                          .filter_by(user_id=current_user.id)
                          .order_by(Submission.submitted_at.desc())
                          .limit(10).all())
    return render_template('auth/profile.html',
                           solved_challenges=solved_challenges,
                           recent_submissions=recent_submissions)
