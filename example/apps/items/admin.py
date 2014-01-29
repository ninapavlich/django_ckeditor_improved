from django.contrib import admin

from .models import *
from .forms import *

class ItemAdmin(admin.ModelAdmin):

    fieldsets = (
        ( 'Item', { 'fields': ( 'parent', ('name', 'txtid'), 'description' ) } ),
    )
    list_display = ['parent', 'name', 'txtid', 'description']

    autocomplete_lookup_fields = { 'fk': ['parent'],}
    raw_id_fields = ('parent',)
    prepopulated_fields = {'txtid': ('name',)}
    
    form = ItemAdminForm

admin.site.register(Item, ItemAdmin)
