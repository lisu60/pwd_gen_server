from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, length, NumberRange, Email


class SeedDetailsForm(FlaskForm):
    site = StringField('Site', validators=[DataRequired(), length(min=5, max=200)])
    month_key = StringField('Month key', validators=[DataRequired(), length(max=100)])
    length_min = IntegerField("Minimum password length", validators=[NumberRange(min=1)])
    length_max = IntegerField("Maximum password length", validators=[DataRequired(), NumberRange(min=1)])
    num = IntegerField("Number characters", validators=[DataRequired(), NumberRange(min=0)], default=1)
    lower = IntegerField("Lower-letter characters", validators=[DataRequired(), NumberRange(min=0)], default=1)
    upper = IntegerField("Upper-letter characters", validators=[DataRequired(), NumberRange(min=0)], default=1)
    special = IntegerField("Special characters", validators=[DataRequired(), NumberRange(min=0)], default=1)
    extra_secret = PasswordField("Extra secret", validators=[DataRequired()])

class EmailPasswordForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])