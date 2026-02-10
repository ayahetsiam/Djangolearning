from django.db import models

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    realisateur = models.ForeignKey('Realisateur', on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name='Date de parution')

# Enregistrement de l'article dans la base de données
Article(titre="Ma première crêpe", auteur="Jean Dupont", contenu="Voici comment faire une délicieuse crêpe bretonne.").save()

# Selection de tous les articles
articles = Article.objects.all()

class Realisateur(models.Model):
    pays= models.CharField(max_length=42)
    nom = models.CharField(max_length=42)
    prenom = models.CharField(max_length=42)
    dateNaissance = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Date de naissance')