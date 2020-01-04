from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

# функция представления index опущена для краткости

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
        title = 'Sign In',
        form = form)