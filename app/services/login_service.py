# -------------------------------------------------------------

from functools import wraps

from flask import (
    flash,
    redirect,
    session,
    url_for,
)

from sqlalchemy import and_

# -------------------------------------------------------------

from app.models.user import User
from app.utils.formats import Format

# -------------------------------------------------------------

from app.configs.database import db

# -------------------------------------------------------------

format = Format()

# -------------------------------------------------------------

class LoginService(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(LoginService, cls).__new__(cls)
        return cls.__instance

    def login(self, username=None, password=None):
        logged = (
            db.session
            .query(User)
            .filter(and_(
                User.username == format.generate_sha512(username), 
                User.password == format.generate_sha512(password))
            )
            .first()
        )
        if logged:
            session['logged'] = True
            return True
        return False
        
    def logout(self):
        session.pop('logged', None)
        return True
    
    @staticmethod
    def login_required(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if "logged" not in session:
                flash('You need to be logged in to access this page.', 'warning')
                return redirect(url_for('login_routes.login'))
            return f(*args, **kwargs)
        return wrap
