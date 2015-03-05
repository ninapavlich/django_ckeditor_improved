CKEditor bundled as a Django app.

This is a fork from https://github.com/espenak/django_ckeditorfiles which has a few changes:

* Change to the default ckeditor image plugin to add figure and figcaption support
* Fix to using CKEditro in inlines


Install
=======

```
    $ pip install django_ckeditor_improved
```

Screenshots
-------

Figure with Figcaption Dialog:
![Screenshot of figure caption dialog](/../master/docs/1_dialog.png?raw=true "Figure caption dialog")
![Screenshot of figure with caption in editor](/../master/docs/2_editor.png?raw=true "Figure with caption in editor")
![Screenshot of figure caption code](/../master/docs/3_code.png?raw=true "Figure caption code")

CKEditors Inline
![Screenshot of ckeditors in inlines](/../master/docs/ckeditors_inline.png?raw=true "Inline editors")

Set Up
-------

#settings.py
1. Image picker set up at /admin/media/imagepicker/
2. Custom ckeditor css file loaded from /static/admin/ckeditor.css

```python
    CKEDITOR_BASIC = {
        'skin': 'moono',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_Full': [
            ['Format', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript','Superscript','SpellChecker', 'SpecialChar', 'Undo', 'Redo'],
            ['NumberedList', 'BulletedList', 'Blockquote'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Iframe','Flash', 'Table', 'HorizontalRule', 'PageBreak'],
            ['PasteText', 'PasteFromWord', 'RemoveFormat'],
            ['showblocks', 'Source', 'Maximize'],
        ],
        'extraPlugins': 'magicline',
        'magicline_everywhere': 'true',
        'magicline_color': '#4fb2d3',
        'toolbar': 'Full',
        'height': 600,
        'width': 1000,
        'filebrowserWindowWidth': 940,
        'filebrowserWindowHeight': 725,
        'filebrowserImageBrowseUrl': '/admin/media/imagepicker/',        
        'forcePasteAsPlainText' : 'true',
    }
```

#admin.py
```python
    class PageAdmin(admin.ModelAdmin):
        form = PageForm
```


#forms.py
```python
    
    from django.conf import settings
    from ckeditorfiles.widgets import CKEditorWidget

    class PageForm(forms.ModelForm):
        class Meta:
            model = Page
            widgets = {
                'content': CKEditorWidget(config=settings.CKEDITOR_BASIC)
            }
```

See https://github.com/espenak/django_ckeditorfiles for further setup and configuration instructions