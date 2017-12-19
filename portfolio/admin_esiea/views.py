from django.utils.text import slugify
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

from admin_esiea.forms import AdminLoginForm

from photo.models import Photo, Video, Contact
from photo.forms import PhotoForm, VideoForm

import hashlib

################## Password hash (sha256) for the admin authentification
ADMIN_HASH = hashlib.sha256(b'esiea2017').hexdigest()
########################################################################


def admin_login(request):
    error = False
    
    form = AdminLoginForm(request.POST or None)
    
    if form.is_valid():
        user = form.cleaned_data['user']
        password_hash = hashlib.sha256(form.cleaned_data['password'].encode()).hexdigest()
        
        if user == 'admin' and password_hash == ADMIN_HASH:
            return redirect(admin, password_hash)
        else:
            error = True
            
    return render(request, 'admin_login.html', {'form': form, 'error': error})
    

def admin(request, password_hash):
    if password_hash == ADMIN_HASH:
        photos = Photo.objects.order_by('-date_ajout')
        videos = Video.objects.order_by('-date_ajout')
        contacts = Contact.objects.order_by('-date_envoi')

        return render(request, 'admin_dashboard.html', {'photos': photos, 'videos': videos, 'contacts': contacts, 'password_hash': password_hash})
    else:
        raise Http404
        
### Photo Admin
        
def photo_add(request, password_hash):
    if password_hash == ADMIN_HASH:
        form = PhotoForm(request.POST or None, request.FILES or None)
        
        if form.is_valid():
            photo = form.save(commit=False)
            photo.slug = slugify(form.cleaned_data['titre'])
            photo.save()
            
            return redirect(admin, password_hash)

        return render(request, 'photo_add.html', {'form': form, 'password_hash': password_hash})
    else:
        raise Http404

def photo_edit(request, id, password_hash):
    if password_hash == ADMIN_HASH:
        photo = get_object_or_404(Photo, id=id)
        form = PhotoForm(request.POST or None, request.FILES or None, instance=photo)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.slug = slugify(form.cleaned_data['titre'])
            photo.save()

            return redirect(admin, password_hash)
        
        return render(request, 'photo_edit.html', {'form': form, 'photo': photo, 'password_hash': password_hash})
    else:
        raise Http404

        
def photo_delete(request, id, password_hash):
    if password_hash == ADMIN_HASH:
        photo = get_object_or_404(Photo, id=id)
        photo.delete()
        
        return redirect(admin, password_hash)
    else:
        raise Http404
    

### Video Admin

def video_add(request, password_hash):
    if password_hash == ADMIN_HASH:
        form = VideoForm(request.POST or None)
        
        if form.is_valid():
            video = form.save(commit=False)
            video.slug = slugify(form.cleaned_data['titre'])
            video.save()
            
            return redirect(admin, password_hash)

        return render(request, 'video_add.html', {'form': form, 'password_hash': password_hash})
    else:
        raise Http404
        
def video_edit(request, id, password_hash):
    if password_hash == ADMIN_HASH:
        video = get_object_or_404(Video, id=id)
        form = VideoForm(request.POST or None, instance=video)
        
        if form.is_valid():
            print("form valid")
            video = form.save(commit=False)
            video.slug = slugify(form.cleaned_data['titre'])
            video.save()

            return redirect(admin, password_hash)
        
        return render(request, 'video_edit.html', {'form': form, 'video': video, 'password_hash': password_hash})
    else:
        raise Http404
    
        
def video_delete(request, id, password_hash):
    if password_hash == ADMIN_HASH:
        video = get_object_or_404(Video, id=id)
        video.delete()
        
        return redirect(admin, password_hash)
    else:
        raise Http404    
