from django.db import models
from peliculas.models import Pelicula
from cinemas.models import Sala
        
class Tarifa(models.Model):
    id_tarifa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=65)
    estado = models.IntegerField()
    valor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarifa'

class Funcion(models.Model):
    id_funcion = models.AutoField(primary_key=True)
    id_pelicula = models.ForeignKey(Pelicula, models.DO_NOTHING, db_column='id_pelicula')
    id_sala = models.ForeignKey(Sala, models.DO_NOTHING, db_column='id_sala')
    id_tarifa = models.ForeignKey(Tarifa, models.DO_NOTHING, db_column='id_tarifa')
    hora_funcion = models.TimeField()
    fecha_funcion = models.DateField()

    class Meta:
        managed = False
        db_table = 'funcion'