from django.db import models

# Create your models here.
class Usuario(models.Model):
    _nombre = models.CharField(max_length=100)
    _contraseña = models.CharField(max_length=100)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def contraseña(self):
        return self._contraseña

    @contraseña.setter
    def contraseña(self, value):
        self._contraseña = value

class Empleado(models.Model):
    _usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    _apellido = models.CharField(max_length=50, unique=True)
    _mail = models.CharField(max_length=100)
    _nombre = models.CharField(max_length=100)
    _telefono = models.CharField(max_length=15)

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, value):
        self._usuario = value

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, value):
        self._mail = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value

class Session(models.Model):
    _usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    _fecha_hora_inicio = models.DateTimeField()
    _fecha_hora_fin = models.DateTimeField()

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, value):
        self._usuario = value

    @property
    def fecha_hora_inicio(self):
        return self._fecha_hora_inicio

    @fecha_hora_inicio.setter
    def fecha_hora_inicio(self, value):
        self._fecha_hora_inicio = value

    @property
    def fecha_hora_fin(self):
        return self._fecha_hora_fin

    @fecha_hora_fin.setter
    def fecha_hora_fin(self, value):
        self._fecha_hora_fin = value