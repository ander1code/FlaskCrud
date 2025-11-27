# -------------------------------------------------------------

from flask import (
    Flask, 
)

# -------------------------------------------------------------

from app.configs.config import Config
from app.configs.database import db
from app.routes.app_routes import app_bp 
from app.routes.login_routes import login_bp
from app.routes.legal_person_routes import legal_person_bp 
from app.routes.natural_person_routes import natural_person_bp 

# -------------------------------------------------------------

def create_app():
    app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
    # config
    app.config.from_object(Config)

    # db_init_app
    db.init_app(app)

    # register_blueprint
    app.register_blueprint(app_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(legal_person_bp)
    app.register_blueprint(natural_person_bp)

    with app.app_context():
        db.create_all()
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=80)


