from django.db import models
from django.contrib.auth.models import AbstractUser

class Empleado(AbstractUser):
    identificacion = models.CharField(unique=True, max_length=25, blank=False, null=False)
    celular = models.CharField(max_length=25, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_perfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='id_perfil')

    class Meta:
        managed = True
        db_table = 'empleado'

class Perfil(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=65)
    estado = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'perfil'