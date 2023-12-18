from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Email, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    name = StringField("Pet's name")

    species = SelectField("Pet's species", choices=[('cat','cat'), ('dog','dog'), ('porcupine','porcupine')])

    photo_url = StringField("Pet's photo", validators=[Optional(), URL(require_tld=False)])

    age = FloatField("Pet's age", validators=[Optional(), NumberRange(min=0, max=30, message='Age must be between 0 to 30')])

    notes = StringField("Pet's notes", validators=[Optional()])

class EditPetForm(FlaskForm):

    photo_url = StringField("Pet's photo", validators=[Optional(), URL(require_tld=False)])

    notes = StringField("Pet's notes", validators=[Optional()])
    
    available = BooleanField("Is the pet available?")