from wtforms.validators import ValidationError

class Validators(object):
    # __instance = None

    # def __new__(cls):
    #     if cls.__instance is None:
    #         cls.__instance = super(Validators, cls).__new__(cls)
    #     return cls.__instance 
    
    def __init__(self, id=None):
        self.id = id

    def validate_name(self, data):
        if not data or not data.strip():
            raise ValidationError('Name is empty.')
        if len(data) < 5:
            raise ValidationError('Invalid name: name must have more than 5 characters.')
        if len(data) > 50:
            raise ValidationError('Invalid name: name must have fewer than 50 characters.')
        return data
    
    def validate_email(self, data):
        if not data or not data.strip():
            raise ValidationError('E-mail is empty.')
        if len(data) < 6:
            raise ValidationError('Invalid e-mail: e-mail must have more than 6 characters.')
        if len(data) > 50:
            raise ValidationError('Invalid e-mail: e-mail must have fewer than 50 characters.')

        import re
        if not re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', data):
            raise ValidationError('Invalid e-mail: invalid e-mail format.')

        from app.models.person import Person
        existing = Person.query.filter_by(email=data).first()
        if self.id is not None:
            if existing and existing.id != int(self.id):
                raise ValidationError('E-mail is already registered.')
        else:
            if existing:
                raise ValidationError('E-mail is already registered.')
        return data

    
    def validate_description(self, data):
        if data: 
            if len(data) < 50:
                raise ValidationError('Invalid description: if filled, it must have more than 50 characters.')
        if len(data) > 200:
            raise ValidationError('Invalid description: description must have fewer than 200 characters.')
        return data
    
    def validate_cpf(self, data):
        
        def validate_cpf_number(cpf: str):
            if not cpf.isdigit() or len(cpf) != 11:
                return False
            if cpf == cpf[0] * 11:
                return False
            soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
            digito1 = (soma * 10) % 11
            digito1 = 0 if digito1 == 10 else digito1
            soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
            digito2 = (soma * 10) % 11
            digito2 = 0 if digito2 == 10 else digito2
            return cpf[-2:] == f"{digito1}{digito2}"

        if not data or not data.strip():
            raise ValidationError('CPF is empty.')
        data = data.replace('.','').replace('-','')
        import re
        if not re.match(pattern=r'^\d{11}$', string=data):
            raise ValidationError('Invalid CPF: invalid CPF format.')
        if not validate_cpf_number(str(data).replace('.','').replace('-','')):
            raise ValidationError('Invalid CPF number.')
        from app.models.natural_person import NaturalPerson
        existing = NaturalPerson.query.filter_by(cpf=data).first()
        if self.id is not None:
            if existing and existing.id != int(self.id):
                raise ValidationError('CPF is already registered.')
        else:
            if existing:
                raise ValidationError('CPF is already registered.')
        return data

    def validate_salary(self, data):
        from decimal import Decimal, InvalidOperation
        if data is None or data == "":
            raise ValidationError('Salary is empty.')
        data_str = str(data)
        salary_str = (
            data_str.replace('R$', '')
                    .replace('.', '')
                    .replace(',', '.')
                    .replace(' ', '')
        )

        try:
            salary_decimal = Decimal(salary_str)
        except InvalidOperation:
            raise ValidationError('Invalid salary: invalid salary format.')

        if salary_decimal < 0:
            raise ValidationError('Salary must be greater than or equal to R$ 0,00.')

        if salary_decimal > Decimal('9999999999.99'):
            raise ValidationError('Invalid salary: salary must be less than R$ 9.999.999.999,99.')
        return salary_decimal

    def validate_birthday(self, data):
        from datetime import date, datetime
        if data is None:
            raise ValidationError('Birthday is empty.')
        try:
            data = datetime.strptime(data, "%d/%m/%Y").date()
        except:
            raise ValidationError('Invalid birthday: expected format DD/MM/YYYY.')
        today = date.today()
        if data > date(today.year - 18, today.month, today.day):
            raise ValidationError('Invalid birthday: must be at least 18 years old.')
        return data

    def validate_gender(self, data):
        if not data or not data.strip():
            raise ValidationError('Gender is empty.')
        if len(data) > 1:
            raise ValidationError('Invalid gender: gender must have 1 characters.')
        if not data in ['M','F','O']:
            raise ValidationError('Invalid gender.')
        return data

    def validate_picture(self, data):
        if self.id is None:
            if data is None or not data:
                raise ValidationError('Picture is empty.')
        return data
    
    def validate_username(self, data):
        if not data or not data.strip():
            raise ValidationError('Username is empty.')
        import re
        if not re.match(pattern=r"^\S+$", string=data):
            raise ValidationError('Invalid username format.')
        return data

    def validate_password(self, data):
        if not data or not data.strip():
            raise ValidationError('Password is empty.')
        return data