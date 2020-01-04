from flask import Flask
from flask import config

app = Flask(__name__)
app.config.from_object('config')

import views