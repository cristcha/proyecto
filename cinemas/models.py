from django.db import models

class Cinema(models.Model):
    id_cinema = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=65)
    direccion = models.CharField(max_length=65)

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'cinema'

class Formato(models.Model):
    id_formato = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'formato'

class Sala(models.Model):
    id_sala = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25)
    capacidad = models.IntegerField()
    estado = models.IntegerField()
    id_formato = models.ForeignKey(Formato, models.DO_NOTHING, db_column='id_formato')
    id_cinema = models.ForeignKey(Cinema, models.DO_NOTHING, db_column='id_cinema')

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'sala'
        