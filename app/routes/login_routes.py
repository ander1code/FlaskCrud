# -------------------------------------------------------------

from flask import (
    Blueprint, 
    flash,
    redirect,
    render_template,
    request, 
    session,
    url_for,
)

from app.forms.login_form import LoginForm
from app.services.login_service import LoginService

# -------------------------------------------------------------

login_bp = Blueprint("login_routes", __name__)
login_service = LoginService()
login_required = login_service.login_required

# -------------------------------------------------------------

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged'):
        flash('User is already logged in.', 'info')
        return redirect(url_for('app_routes.home'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if login_service.login(username=form.username.data, password=form.password.data):
                flash('Successfully logged in.', 'success')
                return redirect(url_for('app_routes.select'))
            else:
                flash('Invalid username and password.', 'danger')
                return redirect(url_for('login_routes.login'))
        return render_template('login/form.html', form=form)
    form = LoginForm()
    return render_template('login/form.html', form=form)

@login_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    login_service.logout()
    flash('Successfully logged out.', 'success')
    return redirect(url_for('app_routes.home'))
