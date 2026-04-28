"""
Academy yo'nalishlari
"""
from flask import Blueprint, render_template
from ..models.database import Lesson

academy_bp = Blueprint('academy', __name__)

@academy_bp.route('/academy')
def index():
    lessons = Lesson.query.filter_by(is_active=True).order_by(Lesson.order_num).all()
    categories = {}
    for lesson in lessons:
        categories.setdefault(lesson.category, []).append(lesson)
    return render_template('academy/index.html', categories=categories)

@academy_bp.route('/academy/<slug>')
def lesson(slug):
    lesson = Lesson.query.filter_by(slug=slug, is_active=True).first_or_404()
    all_lessons = Lesson.query.filter_by(is_active=True).order_by(Lesson.order_num).all()
    idx = next((i for i, l in enumerate(all_lessons) if l.id == lesson.id), 0)
    prev_lesson = all_lessons[idx - 1] if idx > 0 else None
    next_lesson = all_lessons[idx + 1] if idx < len(all_lessons) - 1 else None
    return render_template('academy/lesson.html',
                           lesson=lesson,
                           prev_lesson=prev_lesson,
                           next_lesson=next_lesson)
