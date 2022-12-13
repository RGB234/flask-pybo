from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email
#from wtforms.fields.html5 import EmailField wtforms.fields.html5 에 있는 EmailField 가 wtforms로 옮겨간듯?

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수 입력사항입니다')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력사항입니다')])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력사항입니다')])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    # PasswordField 로 만들면 나중에 폼을 이용해 템플릿 코드를 자동생성할 때 <input type="password">로,
    # EmailFiled 로 만들면 <input type="email"> 이 된다.
    email = EmailField('이메일', [DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

class CommentForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])