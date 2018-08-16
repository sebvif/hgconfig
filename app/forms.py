from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ConfigureForm(FlaskForm):
    submit=SubmitField('Configura el equipo')

class ConfirmForm(FlaskForm):
    submit=SubmitField('Confirma los seriales')

class GoBackForm(FlaskForm):
    submit=SubmitField('Regresa')


class VerifyForm(FlaskForm):
    serial=StringField('Numero de serie', validators=[DataRequired()])
    submit=SubmitField('Revisa la config')
    