"""
Admin panel yo'nalishlari
"""
from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models.database import db, Challenge, User, Submission, Writeup, Lesson

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


def admin_required(f):
    @wraps(f)
    @login_required
    def decorated(*args, **kwargs):
        if not current_user.is_admin:
            flash('Ruxsat yo\'q.', 'danger')
            return redirect(url_for('challenges.index'))
        return f(*args, **kwargs)
    return decorated


@admin_bp.route('/')
@admin_required
def dashboard():
    stats = {
        'users': User.query.count(),
        'challenges': Challenge.query.count(),
        'submissions': Submission.query.count(),
        'correct': Submission.query.filter_by(correct=True).count(),
        'writeups': Writeup.query.count(),
    }
    recent_subs = (Submission.query
                   .order_by(Submission.submitted_at.desc())
                   .limit(20).all())
    return render_template('admin/dashboard.html', stats=stats, recent_subs=recent_subs)


# ── Challengelar ────────────────────────────────────────────────────────────
@admin_bp.route('/challenges')
@admin_required
def challenges():
    challs = Challenge.query.order_by(Challenge.created_at.desc()).all()
    return render_template('admin/challenges.html', challenges=challs)


@admin_bp.route('/challenges/new', methods=['GET', 'POST'])
@admin_required
def new_challenge():
    if request.method == 'POST':
        ch = Challenge(
            title      = request.form['title'],
            description= request.form['description'],
            category   = request.form['category'],
            difficulty = request.form['difficulty'],
            points     = int(request.form.get('points', 100)),
            flag       = request.form['flag'],
            hint       = request.form.get('hint', ''),
            is_active  = 'is_active' in request.form,
        )
        db.session.add(ch)
        db.session.commit()
        flash('Challenge yaratildi!', 'success')
        return redirect(url_for('admin.challenges'))
    return render_template('admin/challenge_form.html', challenge=None)


@admin_bp.route('/challenges/<int:cid>/edit', methods=['GET', 'POST'])
@admin_required
def edit_challenge(cid):
    ch = Challenge.query.get_or_404(cid)
    if request.method == 'POST':
        ch.title       = request.form['title']
        ch.description = request.form['description']
        ch.category    = request.form['category']
        ch.difficulty  = request.form['difficulty']
        ch.points      = int(request.form.get('points', 100))
        ch.flag        = request.form['flag']
        ch.hint        = request.form.get('hint', '')
        ch.is_active   = 'is_active' in request.form
        db.session.commit()
        flash('Challenge yangilandi!', 'success')
        return redirect(url_for('admin.challenges'))
    return render_template('admin/challenge_form.html', challenge=ch)


@admin_bp.route('/challenges/<int:cid>/delete', methods=['POST'])
@admin_required
def delete_challenge(cid):
    ch = Challenge.query.get_or_404(cid)
    db.session.delete(ch)
    db.session.commit()
    flash('Challenge o\'chirildi.', 'info')
    return redirect(url_for('admin.challenges'))


# ── Foydalanuvchilar ─────────────────────────────────────────────────────────
@admin_bp.route('/users')
@admin_required
def users():
    all_users = User.query.order_by(User.score.desc()).all()
    return render_template('admin/users.html', users=all_users)


# ── Writeuplar ────────────────────────────────────────────────────────────────
@admin_bp.route('/writeups')
@admin_required
def writeups():
    all_writeups = Writeup.query.order_by(Writeup.created_at.desc()).all()
    return render_template('admin/writeups.html', writeups=all_writeups)


@admin_bp.route('/writeups/new', methods=['GET', 'POST'])
@admin_required
def new_writeup():
    challenges = Challenge.query.filter_by(is_active=True).all()
    if request.method == 'POST':
        wu = Writeup(
            challenge_id = int(request.form['challenge_id']),
            title        = request.form['title'],
            content      = request.form['content'],
            author       = request.form.get('author', current_user.username),
            is_active    = 'is_active' in request.form,
        )
        db.session.add(wu)
        db.session.commit()
        flash('Writeup yaratildi!', 'success')
        return redirect(url_for('admin.writeups'))
    return render_template('admin/writeup_form.html', writeup=None, challenges=challenges)


# ── Submissions ───────────────────────────────────────────────────────────────
@admin_bp.route('/submissions')
@admin_required
def submissions():
    subs = (Submission.query
            .order_by(Submission.submitted_at.desc())
            .limit(200).all())
    return render_template('admin/submissions.html', submissions=subs)
