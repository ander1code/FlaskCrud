from flask_wtf.form import FlaskForm
from wtforms.fields import StringField, PasswordField
from app.utils.validators import Validators

class LoginForm(FlaskForm):
    
    username = StringField(label='Username', render_kw={
        'class':'form-control',
        'maxlength':'20',
        'value':'admin'
    })
    password = PasswordField(label='Password', render_kw={
        'class':'form-control',
        'maxlength':'20',
    })

    def validate_username(self, field):
        return Validators(id=None).validate_username(field.data)

    def validate_password(self, field):
        return Validators(id=None).validate_password(field.data) 
    