from flask import Blueprint, url_for, current_app
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')
@bp.route('/hello')
def hello_pybo():
    return "Hello pybo"

@bp.route('/')
def index():
    current_app.logger.info("Output at INFO levels")
    return redirect(url_for('question._list'))