from django.db import models

# Create your models here.
class Estudiant(models.Model):
    id_estudiant = models.CharField(max_length=10,blank=False,primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    edad = models.IntegerField(blank=False)
    
    def __str__(self):
        return self.id_estudiant