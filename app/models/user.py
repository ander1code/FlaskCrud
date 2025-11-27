# ------------------------ IMPORT ------------------------

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import validates
from sqlalchemy import String

# ------------------------ CONFIG ------------------------

from app.configs.database import db

# ------------------------ MODELS ------------------------

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(String(128), nullable=False)
    password = db.Column(String(128), nullable=False)

    __table_args__ = (
        UniqueConstraint('username', name='unq_user_username'),
    )

    @validates('username')
    def validate_username(self, key, value):
        from app.utils.validators import Validators
        return Validators().validate_username(value)
    
    @validates('password')
    def validate_password(self, key, value):
        from app.utils.validators import Validators
        return Validators().validate_password(value)