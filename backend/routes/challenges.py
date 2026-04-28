"""
Challenge yo'nalishlari — masalalar ro'yxati, ko'rish, flag topshirish
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from ..models.database import db, Challenge, Submission

challenges_bp = Blueprint('challenges', __name__)


@challenges_bp.route('/')
def index():
    """Bosh sahifa"""
    from ..models.database import User
    total_challenges = Challenge.query.filter_by(is_active=True).count()
    total_users = User.query.count()
    top_users = (User.query
                 .filter(User.score > 0)
                 .order_by(User.score.desc())
                 .limit(5).all())
    recent_solves = (Submission.query
                     .filter_by(correct=True)
                     .order_by(Submission.submitted_at.desc())
                     .limit(10).all())
    return render_template('index.html',
                           total_challenges=total_challenges,
                           total_users=total_users,
                           top_users=top_users,
                           recent_solves=recent_solves)


@challenges_bp.route('/challenges')
def challenges_list():
    """Barcha challengelar"""
    category = request.args.get('category', '')
    difficulty = request.args.get('difficulty', '')

    query = Challenge.query.filter_by(is_active=True)
    if category:
        query = query.filter_by(category=category)
    if difficulty:
        query = query.filter_by(difficulty=difficulty)

    all_challenges = query.order_by(Challenge.points.asc()).all()

    # Foydalanuvchi hal qilgan challengelar
    solved_ids = set()
    if current_user.is_authenticated:
        solved_ids = set(current_user.solved_challenges())

    # Kategoriyalar
    categories = db.session.query(Challenge.category).distinct().all()
    categories = [c[0] for c in categories]

    return render_template('challenges/list.html',
                           challenges=all_challenges,
                           solved_ids=solved_ids,
                           categories=categories,
                           selected_category=category,
                           selected_difficulty=difficulty)


@challenges_bp.route('/challenges/<int:challenge_id>', methods=['GET', 'POST'])
def challenge_detail(challenge_id):
    """Challenge detail va flag topshirish"""
    challenge = Challenge.query.get_or_404(challenge_id)

    solved = False
    show_hint = False

    if current_user.is_authenticated:
        solved = challenge_id in current_user.solved_challenges()
        show_hint = request.args.get('hint') == '1'

    if request.method == 'POST':
        if not current_user.is_authenticated:
            flash('Flag topshirish uchun tizimga kiring.', 'warning')
            return redirect(url_for('auth.login'))

        if solved:
            flash('Siz bu masalani allaqachon hal qildingiz!', 'info')
            return redirect(url_for('challenges.challenge_detail', challenge_id=challenge_id))

        flag_attempt = request.form.get('flag', '').strip()
        is_correct = flag_attempt == challenge.flag

        # Submissionni saqlash
        submission = Submission(
            user_id=current_user.id,
            challenge_id=challenge_id,
            flag_attempt=flag_attempt,
            correct=is_correct,
        )
        db.session.add(submission)

        if is_correct:
            # Ball qo'shish (faqat birinchi marta)
            current_user.score += challenge.points
            flash(f'🎉 To\'g\'ri! +{challenge.points} ball qo\'shildi!', 'success')
        else:
            flash('❌ Noto\'g\'ri flag. Qayta urining!', 'danger')

        db.session.commit()
        return redirect(url_for('challenges.challenge_detail', challenge_id=challenge_id))

    # Writeuplar
    writeups = challenge.writeups.filter_by(is_active=True).all() if solved else []

    return render_template('challenges/detail.html',
                           challenge=challenge,
                           solved=solved,
                           show_hint=show_hint,
                           writeups=writeups)


@challenges_bp.route('/scoreboard')
def scoreboard():
    """Ball jadvali"""
    from ..models.database import User
    users = (User.query
             .filter(User.score > 0)
             .order_by(User.score.desc())
             .limit(100).all())
    return render_template('challenges/scoreboard.html', users=users)
