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

    # .question_view.py 의 Blueprint 객체 'question' 의 routing 함수 _list
    # url_for 은 라우팅 함수의 이름을 인수로 받아 그 함수를 콜링하는 URL 주소를 반환
    # redirect 는 URL 주소를 받아 그 주소로 연결
    return redirect(url_for('question._list'))
