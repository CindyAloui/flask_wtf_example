from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

class GreetUserForm(FlaskForm):
    username = StringField(label=('Enter Your Name:'))
    submit = SubmitField(label=('Submit'))

@app.route('/', methods=('GET', 'POST'))
def index():
    form = GreetUserForm()
    if form.validate_on_submit():
        return f'''<h1> Welcome {form.username.data} </h1>'''
    return render_template('index.html', form=form)
