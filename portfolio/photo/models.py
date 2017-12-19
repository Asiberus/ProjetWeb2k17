from django.db import models

class Photo(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to="photo/")
    date_photo = models.DateField(null=True, auto_now_add=False, auto_now=False, verbose_name="Date de la photo")
    date_ajout = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.titre
    
class Video(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    lien = models.URLField(max_length=100)
    date_video = models.DateField(null=True, auto_now_add=False, auto_now=False, verbose_name="Date de la vidéo")
    date_ajout = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'ajout")
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.titre
    
class Contact(models.Model):
    sujet = models.CharField(max_length=100)
    message = models.TextField()
    envoyeur = models.EmailField()
    date_envoi = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date d'envoi")
    
    def __str__(self):
        return self.sujet
