from django.db import models

        
class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'genero'
        

class Clasificacion(models.Model):
    id_clasificacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'clasificacion'
        
class Pelicula(models.Model):
    id_pelicula = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    poster = models.ImageField(upload_to='images')
    sinopsis = models.CharField(max_length=1000)
    reparto = models.CharField(max_length=150)
    director = models.CharField(max_length=50)
    fecha_estreno = models.DateField()
    trailer = models.CharField(max_length=150)
    duracion = models.IntegerField()
    id_genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='id_genero')
    id_clasificacion = models.ForeignKey(Clasificacion, models.DO_NOTHING, db_column='id_clasificacion')

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = False
        db_table = 'pelicula'
