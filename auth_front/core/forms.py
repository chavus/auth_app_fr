from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, EqualTo, InputRequired


class ItemForm(FlaskForm):
    item = StringField('Item', validators=[InputRequired()])
    submit = SubmitField('Search Item')


