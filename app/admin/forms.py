from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    usuario = StringField('Usuario',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class BiografiaForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    resumen = StringField('Resumen')
    rol = StringField('Rol',validators=[DataRequired()])
    foto = StringField('Foto',validators=[DataRequired()])
    ubicacion = StringField('Ubicacion',validators=[DataRequired()])
    cv = StringField('CV',validators=[DataRequired()])
    github = StringField('Url GitHub',validators=[DataRequired()])
    linkedin = StringField('Url linkedIn',validators=[DataRequired()])
    twitter = StringField('Url Twitter',validators=[DataRequired()])
    submit = SubmitField('Actualizar Datos')

class ProyectoForm(FlaskForm):
    codigo = StringField('Codigo',validators=[DataRequired()])
    nombre = StringField('Nombre',validators=[DataRequired()])
    descripcion = StringField('Descripción',validators=[DataRequired()])
    imagen = StringField('Imagen',validators=[DataRequired()])
    url = StringField('Url',validators=[DataRequired()])
    submit = SubmitField('Guardar')