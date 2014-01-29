import reversion

from django.contrib import admin
from django.db import models

from imagekit.admin import AdminThumbnail

from .models import Image

class ImageAdmin(reversion.VersionAdmin):
    
    admin_thumbnail = AdminThumbnail(image_field='admin_thumbnail')
    csv_fields = [
        'image', 'credit', 'description', 'content_tag',
        'created_by', 'created', 'modified_by', 'modified']

    fieldsets = (
        ( 'Core Data', { 
            'fields': ( 
                ('image'),
                ('credit'),
                ('caption'),
                ('description',),
            )
        }),        
    )
    search_fields = ('credit', 'caption', 'description')
    
    list_display = ('__unicode__', 'credit', 'caption', 'description', 'non_linking_thumbnail')

    def non_linking_thumbnail   (self, obj):
        return u'<img src="%s" />' % obj.admin_thumbnail.url        
    non_linking_thumbnail.allow_tags = True


admin.site.register(Image, ImageAdmin)
