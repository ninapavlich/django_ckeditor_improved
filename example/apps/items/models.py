from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class Item( models.Model ):
    parent = models.ForeignKey('self', null = True, blank = True )

    name = models.CharField( _("Name"), max_length = 255, blank = False )
    txtid = models.CharField( _("Text ID"), max_length = 255, 
        blank = True, unique = True )

    description =  models.TextField( _('Description'), blank=True, null=True )


    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains","description__icontains",)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = [ "name" ]
