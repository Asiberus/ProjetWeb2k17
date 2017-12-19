from django import forms
from django.contrib.admin import widgets
from photo.models import Contact, Photo, Video

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('date_envoi',)
        
class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('date_ajout', 'slug')
        
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = ('date_ajout', 'slug')
    