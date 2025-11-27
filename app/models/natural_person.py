# ------------------------ IMPORT ------------------------

from sqlalchemy import CheckConstraint, UniqueConstraint, Numeric
from sqlalchemy.orm import validates
from sqlalchemy import Integer, String, Date, ForeignKey

# ------------------------ CONFIG ------------------------

from app.configs.database import db

# ------------------------ MODELS ------------------------

class NaturalPerson(db.Model):
    __tablename__ = 'naturalpersons'
    
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    person_id = db.Column(Integer, ForeignKey('persons.id'), nullable=False)
    person = db.relationship('Person', backref='natural_person', uselist=False)
    cpf = db.Column(String(11), nullable=False)
    gender = db.Column(String(1), nullable=False)
    salary = db.Column(Numeric(10,2), nullable=False)
    birthday = db.Column(Date, nullable=False)
    picture = db.Column(String(200), nullable=False)

    def __init__(self, cpf, gender, salary, birthday, picture):
        from app.utils.validators import Validators
        self.validators = Validators()
        self.cpf = cpf
        self.gender = gender
        self.salary = salary
        self.birthday = birthday
        self.picture = picture
      
    @validates('cpf')
    def validate_cpf(self, key, value):
        from app.utils.validators import Validators
        return Validators(id=self.id).validate_cpf(value)
    
    @validates('salary')
    def validate_salary(self, key, value):
        from app.utils.validators import Validators
        return Validators(id=self.id).validate_salary(value)
    
    @validates('birthday')
    def validate_birthday(self, key, value):
        from app.utils.validators import Validators
        return Validators(id=self.id).validate_birthday(value)
    
    @validates('gender')
    def validate_gender(self, key, value):
        from app.utils.validators import Validators
        return Validators(id=self.id).validate_gender(value)
    
    @validates('picture')
    def validate_picture(self, key, value):
        from app.utils.validators import Validators
        return Validators(id=self.id).validate_picture(value)

    __table_args__ = (
        UniqueConstraint('cpf', name='unq_naturalperson_cpf'),
        CheckConstraint("gender IN ('M','F','O')", name='chk_naturalperson_gender'),
        CheckConstraint('salary > 0 AND salary <= 9999999999.99', name='chk_naturalperson_salary'),
    )