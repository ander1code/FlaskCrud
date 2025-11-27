# ------------------------ IMPORT ------------------------

from datetime import datetime
from sqlalchemy import CheckConstraint, UniqueConstraint
from sqlalchemy.orm import validates
from sqlalchemy import Integer, String, Boolean, DateTime

# ------------------------ CONFIG ------------------------

from app.configs.database import db

# ------------------------ MODELS ------------------------

class Person(db.Model):
    __tablename__ = 'persons'
    
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(50), nullable=False)
    email = db.Column(String(50), nullable=False)
    status = db.Column(Boolean, nullable=False, default=False)
    description = db.Column(String(200), nullable=True)
    created_at = db.Column(DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, name, email, status, description):
        self.name = name
        self.email = email
        self.status = status
        self.description = description
    
    @validates('name')
    def validate_name(self, key, value):
        from app.utils.validators import Validators
        return Validators(id=self.id).validate_name(value)
    
    @validates('email')
    def validate_email(self, key, value):
        from app.utils.validators import Validators
        return Validators(id=self.id).validate_email(value)
    
    @validates('description')
    def validate_description(self, key, value):
        from app.utils.validators import Validators
        return Validators(id=self.id).validate_description(value)

    __table_args__ = (
        UniqueConstraint('email', name='unq_person_email'),
        CheckConstraint('updated_at >= created_at', name='chk_updated_at_person'),
    )




