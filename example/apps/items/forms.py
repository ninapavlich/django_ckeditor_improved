from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import *

class ItemAdminForm(forms.ModelForm):
    description =  forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Item
