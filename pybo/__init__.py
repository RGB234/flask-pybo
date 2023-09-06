from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flaskext.markdown import Markdown

# import config  현재 config.py 파일은 삭제됨

naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
#######################
# AWS 무료체험기간이 1달이므로 아끼기위해 아직 AWS 무료체험판 사용하지않음
# AWS 서버관련 설정 구현은 했으나 설명은 대부분 하지않았음
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def page_not_found(e):
    return render_template('404.html'), 404


def create_app():
    app = Flask(__name__)
    # app.config.from_object(config)
    # ../../venvs/myproject.cmd 파일의 @set APP_CONFIG_FILE=D:\Study\flaskProjects\myproject\config\development.py
    app.config.from_envvar('APP_CONFIG_FILE')

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    from . import models

    # 가장 먼저 실행되는 파일인 __init__.py 에 blueprint 들을 등록.
    # blueprint 들은 url 주소를 받아 그에 대응하는 라우팅 함수를 실행
    # blueprint
    from .views import main_views, question_views, answer_views, auth_views, comment_views, vote_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(vote_views.bp)

    # 필터
    from .filter import format_datetime
    # 'datetime'이라는 이름으로 format_datetime이라는 필터 등록
    app.jinja_env.filters['datetime'] = format_datetime

    # markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])
    # 오류페이지
    app.register_error_handler(404, page_not_found)

    return app
