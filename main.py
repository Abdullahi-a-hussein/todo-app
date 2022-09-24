from flask import render_template, redirect, url_for, flash, request, Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, logout_user, login_required, UserMixin, login_user, login_manager
from datetime import datetime




# App initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Assddk8hsMt3hhy'

@app.route('/')
def home():
    today = datetime.today().strftime('%d')
    return render_template('index.html', today=today)


if __name__ == "__main__":
    app.run(debug=True)