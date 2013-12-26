from flask.ext.wtf import Form
from wtforms  import TextField, BooleanField, TextAreaField
from wtforms.validators  import Required, Length, ValidationError
from app.models import User

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

class MyLoginForm(Form):
    username = TextField('username', validators = [Required()])
    email = TextField('email', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

    def validate_login(self, field):
        if self.get_user() is None:
            raise ValidationError('Invalid User.')


    def get_user(self):
        return User.query.filter_by(nickname=self.username.data).first()

class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use, Please choose another one.')
            return False

        return True

class PostForm(Form):
    post = TextField('post', validators = [Required()])

class SearchForm(Form):
    search = TextField('search', validators= [Required()])