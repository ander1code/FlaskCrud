from flask_wtf.form import FlaskForm
from wtforms.fields import StringField, BooleanField, TextAreaField
from app.utils.validators import Validators

class PersonForm(FlaskForm):

    def __init__(self, id=None, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

    name = StringField(label='Name', render_kw={
        'class':'form-control',
        'maxlength':'50',
    })

    email = StringField(label='E-mail', render_kw={
        'class':'form-control',
        'maxlength':'50',
    })

    status = BooleanField(label='Status', default=False, render_kw={
        'class':'form-control'
    })

    description = TextAreaField(label='Description', render_kw={
        'class':'form-control',
        'maxlength':'200',
    })

    def validate_name(self, field):
        return Validators(id=self.id).validate_name(field.data)
    
    def validate_email(self, field):
        return Validators(id=self.id).validate_email(field.data)
    
    def validate_description(self, field):
        return Validators(id=self.id).validate_description(field.data)
    


