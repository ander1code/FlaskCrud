class NaturalPersonDTO(object):
    def __init__(self, form_data):
        self.name = form_data['name']
        self.email = form_data['email']
        self.status = form_data['status']
        self.description = form_data['description']
        self.cpf = form_data['cpf']
        self.gender = form_data['gender']
        self.salary = form_data['salary']
        self.birthday = form_data['birthday']
        self.picture = form_data['picture']
    
    def get_salary_decimal(self):
        from decimal import Decimal, InvalidOperation
        if not self.salary:
            raise ValueError("Salary is empty")
        value_str = self.salary.replace('R$','').replace('.','').replace(',','.').replace(' ','')
        try:
            return Decimal(value_str)
        except InvalidOperation:
            raise ValueError("Invalid salary format")
