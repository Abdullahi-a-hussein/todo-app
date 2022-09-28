from flask import render_template, redirect, url_for, flash, request, Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, logout_user, login_required, UserMixin, login_user, login_manager
from datetime import datetime




# App initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Assddk8hsMt3hhy'


TODAY = datetime.today().strftime('%d')


# ---------------------------------- Database Tables Set up ------------------------------------ #
CATEGORY = [{'name': 'Grocery', 'color': 'blue'}, {'name': 'Study', 'color': 'red'}]



@app.route('/')
def home():
    return render_template('index.html', today=TODAY, category=CATEGORY)

@app.route('/today')
def today():
    return render_template('today.html', today=TODAY, category=CATEGORY)

@app.route('/scheduled')
def scheduled():
    return render_template('scheduled.html', today=TODAY, category=CATEGORY)

@app.route('/all')
def all():
    return render_template('all.html', today=TODAY, category=CATEGORY)
@app.route('/add-list', methods=['GET', 'POST'])
def add_list():
    if request.method == 'POST':
        name = request.form.get('name')
        color = request.form.get('color')
        CATEGORY.append({'name': name, 'color': color})
        return redirect(url_for('home'))
        
 

if __name__ == "__main__":
    app.run(debug=True)