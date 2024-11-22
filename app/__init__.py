from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'never_guess_secret_key'

from app import routes  # noqa: E402