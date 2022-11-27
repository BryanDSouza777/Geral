from django.db import models

# Create your models here.
class Animes(models.Model):
    nome = models.CharField(max_length=255)
    episodios = models.CharField(max_length=255, blank=True)
    temporadas = models.CharField(max_length=255, blank=True)
    lançamento = models.DateField()
    sinopse = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank = True, upload_to='fotos/%Y/%m/%d')

    def __str__(self):
        return self.nome

class TipoHardware(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Hardware(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    peça = models.ForeignKey(TipoHardware,on_delete=models.CASCADE)
    especificações = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank = True, upload_to='fotos/%Y/%m/%d')

    def __str__(self):
        return self.modelo

class Jogos(models.Model):
    nome = models.CharField(max_length=255)
    lançamento = models.DateField()
    desenvolvedora = models.CharField(max_length=255)
    descrição = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank = True, upload_to='fotos/%Y/%m/%d')

    def __str__(self):
        return self.nome