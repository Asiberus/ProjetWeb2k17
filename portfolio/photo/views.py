from django.utils.text import slugify
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from photo.models import Photo, Video
from photo.forms import ContactForm


def photo_show_all(request):
    photos = Photo.objects.order_by('-date_ajout')
    
    return render(request, 'photo/photo_show_all.html', {'photos': photos})

def photo_show_one(request, slug):
    photo = get_object_or_404(Photo, slug=slug)
    
    if photo.date_ajout == Photo.objects.order_by('-date_ajout')[0].date_ajout:
        isFirst = True
    else:
        isFirst = False
    
    return render(request, 'photo/photo_show_one.html', {'photo': photo, 'isFirst': isFirst})



def video_show_all(request):
    videos = Video.objects.order_by('-date_ajout')
    
    return render(request, 'video/video_show_all.html', {'videos': videos})

def video_show_one(request, slug):
    video = get_object_or_404(Video, slug=slug)
    
    return render(request, 'video/video_show_one.html', {'video': video})


def contact(request):
    form = ContactForm(request.POST or None)
    
    for field in form:
        field.css_classes(extra_classes='form-group')
        print(field)
    
    if form.is_valid():
        form.save()
        envoi = True
        form = ContactForm()
        
        
    return render(request, 'contact.html', locals())



