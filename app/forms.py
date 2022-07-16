from flask_wtf import FlaskForm
import wtforms as wf


class UserForm(FlaskForm):
    username = wf.StringField('Имя пользователя', validators=[wf.validators.DataRequired()])
    password = wf.PasswordField('Пароль', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('OK')


class CustomerForm(FlaskForm):
    name = wf.StringField('ФИО', validators=[wf.validators.DataRequired()])
    phone_number = wf.StringField('Телефонный номер', validators=[wf.validators.DataRequired()])
    item = wf.StringField('Наименование товара', validators=[wf.validators.DataRequired()])
    quantity = wf.IntegerField('Количество', validators=[wf.validators.DataRequired()])
    price = wf.IntegerField('Цена товара', validators=[wf.validators.DataRequired()])
    submit = wf.SubmitField('OK')
