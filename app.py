from flask import render_template, flash, request, url_for, redirect, session
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from flask_mail import Message
from flask_mail import Mail

from flask import Flask, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager ,  UserMixin, \
                                login_required, login_user, logout_user

from flask_wtf.csrf import CsrfProtect 


app = Flask(__name__)
app.secret_key = 'very secret'
csrf = CsrfProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)

mail = Mail()
mail.init_app(app)

@app.route("/message")
def message():
    with mail.connect() as conn:
        subject = "hello, %s" % "taras"
        msg = Message("Hello",
                  sender="taraslaz10@ukr.net",
                  recipients=["taraslazpro1997@gmail.com"])

        conn.send(msg)

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Submit')

"""class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
"""
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return render_template('login.html', form=form)

"""@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # следущий код выполняется при методе запроса GET
    # или при признании полномочий недействительными
    return render_template('login.html', error=error)
"""
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/taras")
def taras():
    title = "Тархун"
    return render_template('taras.html', title = title)

@app.route("/grab")
def grab():
    title = "Grabon"
    return render_template('grab.html', title = title)

@app.route("/zenya")
def zenya():
    title = "Zenya"
    return render_template('zenya.html', title = title)

@app.route("/trush")
def trush():
    title = "Trush"
    return render_template('trush.html', title = title)

@app.route("/vetal")
def vetal():
    title = "Vetal"
    return render_template('vetal.html', title = title)

@app.route("/boyarka")
def boyarka():
    title = "Боярка лучший район"
    return render_template('boyarka.html', title = title)

@app.route("/seroga")
def seroga():
    title = "Серога"
    return render_template('seroga.html', title = title)

@app.route("/yaric")
def yaric():
    title = "Ярик"
    return render_template('yaric.html', title = title)

@app.route("/andriy")
def andriy():
    title = "Андрюха"
    return render_template('andriy.html', title = title)

@app.route("/rupra")
def rupra():
    title = "Зупрапраганда"
    return render_template('rupra.html', title = title)

@app.route("/contacs")
def contact():
    title = "Контакти"
    return render_template('contacts.html', title = title)

@app.route('/index')
def index():
    return 'Index Page'

@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # показать профиль данного пользователя
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # вывести сообщение с данным id, id - целое число
    return 'Post %d' % post_id



@app.route('/list')
def listo():
    user = {'nickname': 'Эльдар Рязанов'}
    posts = [
        {
            'author':  'John' ,
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': 'Susan',
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': 'Ипполит',
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

if __name__ == '__main__':
    app.run()