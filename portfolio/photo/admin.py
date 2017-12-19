from django.contrib import admin
from django.utils.text import Truncator
from .models import Photo, Video, Contact

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('titre', 'apercu_contenu', 'photo', 'date_ajout')
    list_filter = ('date_ajout',)
    date_hierarchy = 'date_ajout'
    ordering = ('date_ajout', )
    search_fields = ('titre', 'description')
    prepopulated_fields = {'slug': ('titre',),}
    
    fields = ('titre', 'slug', 'date_photo', 'photo', 'description')
    
    def apercu_contenu(self, photo):
        return Truncator(photo.description).chars(40, truncate='...')

    apercu_contenu.short_description = 'Aperçu de la description'
    
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titre', 'apercu_contenu', 'date_ajout',)
    list_filter = ('date_ajout',)
    date_hierarchy = 'date_ajout'
    ordering = ('date_ajout',)
    search_fields = ('titre', 'description',)
    prepopulated_fields = {'slug': ('titre',),}
    
    fields = ('titre', 'slug', 'date_video', 'lien', 'description')
    
    def apercu_contenu(self, video):
        return Truncator(video.description).chars(40, truncate='...')
    
    apercu_contenu.short_descrition = 'Aperçu de la description'
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('sujet', 'apercu_contenu', 'envoyeur', 'date_envoi',)
    list_filter = ('date_envoi',)
    date_hierarchy = 'date_envoi'
    ordering = ('date_envoi',)
    search_fields = ('sujet', 'message', 'envoyeur')
    
    fields = ('envoyeur', 'sujet', 'message')
    
    def apercu_contenu(self, contact):
        return Truncator(contact.message).chars(40, truncate='...')
    apercu_contenu.short_description = 'Apercu du message'
    
    
admin.site.register(Video, VideoAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Contact, ContactAdmin)


