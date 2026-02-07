from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, FloatField, RadioField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    matricula = IntegerField(
        "Matricula",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.NumberRange(min=100, max=1000, message="Ingrese valor valido"),
        ],
    )
    nombre = StringField(
        "Nombre",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.length(min=3, max=10, message="Ingrese nombre valido"),
        ],
    )
    apaterno = StringField(
        "Apaterno", [validators.DataRequired(message="El campo es requerido")]
    )
    amaterno = StringField(
        "Amaterno", [validators.DataRequired(message="El campo es requerido")]
    )
    correo = EmailField("Correo", [validators.Email(message="Ingresa correo valido")])


class CinepolisForm(Form):
    nombre = StringField(
        "Nombre",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.length(
                min=2, max=15, message="El nombre debe tener entre 2 y 15 caracteres"
            ),
        ],
    )

    compradores = IntegerField(
        "Compradores",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.NumberRange(min=1, message="Debe ingresar al menos 1 comprador"),
        ],
    )

    boletos = IntegerField(
        "Boletos",
        [
            validators.DataRequired(message="El campo es requerido"),
            validators.NumberRange(min=1, message="Debe ingresar al menos 1 boleto"),
        ],
    )

    cineco = RadioField(
        "¿Paga con tarjeta CINECO?",
        choices=[("si", "Sí"), ("no", "No")],
        default="no",
        validators=[validators.DataRequired(message="El campo es requerido")],
    )
