from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit

class Image( models.Model ):
    image = models.ImageField(upload_to='media/image/')
    credit = models.CharField(max_length=255, blank=True)
    caption = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True,
        help_text="Description of the image (not the image caption), used "
                  "within the image alt tag.")

    # -- Images
    admin_thumbnail = ImageSpecField( source='image', format='JPEG',
        processors=[ResizeToFit(250, 250)], options={'quality': 80})

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "credit__icontains","caption__icontains","description__icontains",)

    def __unicode__(self):
        return u"Image-%s" % str(self.pk).zfill(6)
