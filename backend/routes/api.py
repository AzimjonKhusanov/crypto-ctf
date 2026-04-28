"""
API yo'nalishlari — JSON endpointlar
"""
from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from ..models.database import db, Challenge, User, Submission

api_bp = Blueprint('api', __name__)


@api_bp.route('/challenges')
def get_challenges():
    challenges = Challenge.query.filter_by(is_active=True).all()
    return jsonify([{
        'id': c.id,
        'title': c.title,
        'category': c.category,
        'difficulty': c.difficulty,
        'points': c.points,
        'solves': c.solve_count(),
    } for c in challenges])


@api_bp.route('/scoreboard')
def get_scoreboard():
    users = User.query.filter(User.score > 0).order_by(User.score.desc()).limit(50).all()
    return jsonify([{
        'rank': i + 1,
        'username': u.username,
        'score': u.score,
        'solved': len(u.solved_challenges()),
    } for i, u in enumerate(users)])


@api_bp.route('/submit', methods=['POST'])
@login_required
def submit_flag():
    data = request.get_json()
    challenge_id = data.get('challenge_id')
    flag = data.get('flag', '').strip()

    challenge = Challenge.query.get(challenge_id)
    if not challenge:
        return jsonify({'success': False, 'message': 'Challenge topilmadi'}), 404

    already_solved = challenge_id in current_user.solved_challenges()
    if already_solved:
        return jsonify({'success': False, 'message': 'Allaqachon hal qilingan'})

    correct = flag == challenge.flag
    sub = Submission(
        user_id=current_user.id,
        challenge_id=challenge_id,
        flag_attempt=flag,
        correct=correct,
    )
    db.session.add(sub)
    if correct:
        current_user.score += challenge.points
    db.session.commit()

    return jsonify({
        'success': correct,
        'message': f'+{challenge.points} ball!' if correct else 'Noto\'g\'ri flag',
        'points': challenge.points if correct else 0,
    })


@api_bp.route('/stats')
def get_stats():
    return jsonify({
        'total_challenges': Challenge.query.filter_by(is_active=True).count(),
        'total_users': User.query.count(),
        'total_solves': Submission.query.filter_by(correct=True).count(),
    })
