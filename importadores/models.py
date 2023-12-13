from django.db import models

# Create your models here.
class Importador(models.Model):
    id_importador   = models.AutoField(primary_key=True)
    nombre          = models.CharField(max_length=30)
    descripcion     = models.CharField(max_length=200)
    direccion       = models.CharField(max_length=50)
    representante   = models.CharField(max_length=30)
    pais            = models.CharField(max_length=30)
    email           = models.CharField(max_length=35) 
    fono            = models.IntegerField()        
    
    def __str__(self):
        return "ID: "+str(self.id_importador)+" "+str(self.nombre)+" /"+str(self.representante)