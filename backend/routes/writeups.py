"""
Writeup yo'nalishlari
"""
from flask import Blueprint, render_template
from ..models.database import Writeup, Challenge

writeups_bp = Blueprint('writeups', __name__)

@writeups_bp.route('/writeups')
def index():
    writeups = (Writeup.query
                .filter_by(is_active=True)
                .order_by(Writeup.created_at.desc())
                .all())
    return render_template('writeups/index.html', writeups=writeups)

@writeups_bp.route('/writeups/<int:writeup_id>')
def detail(writeup_id):
    writeup = Writeup.query.get_or_404(writeup_id)
    return render_template('writeups/detail.html', writeup=writeup)
