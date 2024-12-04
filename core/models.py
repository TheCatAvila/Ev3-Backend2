from django.db import models

# Create your models here.
from django.db import models

class Ocupacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre 

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    ocupacion = models.ManyToManyField(Ocupacion)  # Cambiado a ManyToManyField
    verificado = models.BooleanField(default=False)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars/')
    linkedin = models.CharField(max_length=100, null=True)
    whatsapp = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nombre 

class Episodio(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.CharField(max_length=50)
    numero = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    anfitrion = models.ForeignKey(Persona, on_delete=models.CASCADE)
    suscriptores = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comentarios = models.IntegerField(default=0)
    descargas = models.IntegerField(default=0)
    imagen = models.ImageField(blank=True, null=True, upload_to='episodios/')