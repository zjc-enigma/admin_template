from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, FloatField

class RegistrationForm(Form):
    date = StringField('date', [validators.Length(10)])

    bonus_cvt = IntegerField('bonus cvt', [
        validators.DataRequired(),
        #validators.Length(min=1)
    ])
    total_cvt = IntegerField('total cvt', [
        validators.DataRequired(),
        #validators.Length(min=1)
    ])
    bonus_cost = FloatField('bonus cost', [
        validators.DataRequired(),
        #validators.Length(min=1)
    ])
    total_cost = FloatField('total cost', [
        validators.DataRequired(),
        #validators.Length(min=1)
    ])
    bonus_imp = IntegerField('bonus imp', [
        validators.DataRequired(),
        #validators.Length(min=1)
    ])
    total_imp = IntegerField('total imp', [
        validators.DataRequired(),
        #validators.Length(min=1)    
    ])
