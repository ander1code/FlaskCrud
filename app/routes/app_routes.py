# -------------------------------------------------------------

from flask import (
    Blueprint, 
    jsonify,
    render_template, 
    session, 
)

from app.services.login_service import LoginService
from app.utils.modal import Modal

# -------------------------------------------------------------

app_bp = Blueprint("app_routes", __name__)
modal = Modal()
login_service = LoginService()
login_required = login_service.login_required

# -------------------------------------------------------------

@app_bp.route('/', methods=['GET'])
def home():
    from datetime import date
    session['current_year'] = date.today().year
    return render_template('home/home.html')

@app_bp.route('/select', methods=['GET'])
@login_required
def select():
    return render_template('person/select.html')

@app_bp.route('/clean_modal', methods=['POST'])
def clean_modal():
    modal.clear_modal(session)
    return jsonify({})

