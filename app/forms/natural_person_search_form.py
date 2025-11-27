from flask_wtf.form import FlaskForm
from wtforms.fields import StringField

class NaturalPersonSearchForm(FlaskForm):
    search = StringField(label='Search', render_kw={
        'class':'form-control',
        'maxlength':'50',
    })


    
