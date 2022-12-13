from pybo import db #db는 __init__ 에서 생성한 SQLAlchemy 객체

#ManyToMany 관계 정의, 하나의 유저는 여럿(Many)의 질문을, 하나의 질문은 여럿(Many)의 유저와 관계(좋아요기능)를 형성
question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey(
        'question.id', ondelete='CASCADE'), primary_key=True)
)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    subject = db. Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    #server_default 는 default 파라미터(?)와 다르게 기존 db 데이터에도 적용
    #user_id 는 User 모델 데이터의 id 값을 Qeustion 모델에 포함시키기 위함
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    #User 모델 데이터를 통해 Question모델 데이터 참조를 위함, question 객체 생성시 user = g.user() 대입
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    #voter 는 User 모델과 question_voter 테이블을 참조하여 다대다 관계(두 모델 간에 두 개 이상의 relationship)를 형성
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))

answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey(
        'answer.id', ondelete='CASCADE'), primary_key=True)
)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #db.ForeignKey(연결할 기존 모델의 속성, ondelete삭제 연동) / render_template  할 때 question 값이 전달됨
    question_id = db.Column(db.Integer, 
                                db.ForeignKey('question.id', ondelete='CASCADE'))
    #db.relationship 기존 모델 참조 (참조할 모델, 역참조backref)
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    modify_date = db.Column(db.DateTime())
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), nullable=True)
    question = db.relationship('Question', backref=db.backref('comment_set'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), nullable=True)
    answer = db.relationship('Answer', backref=db.backref('comment_set'))