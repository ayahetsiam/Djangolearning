from django.db import models

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    categorie = models.ForeignKey('Categorie', null = True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='Date de parution')

    def __str__(self):
        return self.titre

class Categorie(models.Model):
    nom= models.CharField(max_length=100)

    def __str__(self):
        return self.nom