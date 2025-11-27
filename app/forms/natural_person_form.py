from wtforms.fields import StringField, FileField, SelectField
from app.utils.validators import Validators
from app.forms.person_form import PersonForm

class NaturalPersonForm(PersonForm):

    def __init__(self, id=None, *args, **kwargs):
        self.id = id
        super(NaturalPersonForm, self).__init__(*args, **kwargs)
    
    __GENDERS = (
        ('M','Male'),('F','Female'),('O','Other')
    )

    cpf = StringField(label='CPF', render_kw={
        'class':'form-control',
        'maxlength':'14',
    })

    salary = StringField(label='Salary', render_kw={
        'class':'form-control',
        'maxlength':'15',
    })

    birthday = StringField(label='Birthday', render_kw={
        'class':'form-control',
        'maxlength':'10',
    })

    gender =  SelectField(label='Gender', choices=__GENDERS, render_kw={
        'class':'form-control',
        'maxlength':'1',
    })

    picture = FileField(label='Picture', render_kw={
        'class':'form-control'
    })

    def validate_cpf(self, field):
        return Validators(id=self.id).validate_cpf(field.data)

    def validate_salary(self, field):
        return Validators(id=self.id).validate_salary(field.data)

    def validate_birthday(self, field):
        return Validators(id=self.id).validate_birthday(field.data)

    def validate_gender(self, field):
        return Validators(id=self.id).validate_gender(field.data)

    def validate_picture(self, field):
        return Validators(id=self.id).validate_picture(field.data)
    
    
