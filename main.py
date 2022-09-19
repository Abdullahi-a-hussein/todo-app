from flask import render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, logout_user, login_required, UserMixin, login_user, login_manager
from datetime import datetime