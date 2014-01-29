from django import forms
from ckeditorfiles.widgets import CKEditorWidget

from .models import *

class ItemAdminForm(forms.ModelForm):
    description =  forms.CharField(widget=CKEditorWidget(config=settings.CKEDITOR_BASIC), required=False)
    class Meta:
        model = Item
