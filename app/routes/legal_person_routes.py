# -------------------------------------------------------------

from flask import (
    Blueprint, 
    redirect,
    session, 
    url_for,
)

from app.services.login_service import LoginService
from app.utils.modal import Modal

# -------------------------------------------------------------

legal_person_bp = Blueprint("legal_person_routes", __name__)
modal = Modal()
login_service = LoginService()
login_required = login_service.login_required

# -------------------------------------------------------------

@legal_person_bp.route('/legal', methods=['POST', 'GET'])
@login_required
def legal_list():
    modal.show_modal(session, 'Information', 'Legal Person is not implemented!')
    return redirect(url_for('app_routes.select'))

# -------------------------------------------------------------