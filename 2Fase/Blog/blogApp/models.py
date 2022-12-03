from django.db import models

# Create your models here.
class Animes(models.Model):
    nome = models.CharField(max_length=255)
    episodios = models.IntegerField(blank=True)
    temporadas = models.IntegerField(blank=True)
    lançamento = models.DateField()
    sinopse = models.TextField(blank=True)
    sinopse2 = models.TextField(blank=True)
    sinopse3 = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank = True, upload_to='fotos/%Y/%m/%D')

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
    lançamento = models.DateField()
    especificações = models.TextField(blank=True)
    especificações2 = models.TextField(blank=True)
    especificações3 = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank = True, upload_to='fotos/%Y/%m/%D')

    def __str__(self):
        return self.nome

class Jogos(models.Model):
    nome = models.CharField(max_length=255)
    lançamento = models.DateField()
    desenvolvedora = models.CharField(max_length=255)
    descrição = models.TextField(blank=True)
    descrição2 = models.TextField(blank=True)
    descrição3 = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank = True, upload_to='fotos/%Y/%m/%D')

    def __str__(self):
        return self.nome