CKEditor bundled as a Django app.

This is a fork from https://github.com/espenak/django_ckeditorfiles which has a few changes:

* Change to the default ckeditor image plugin to add figure and figcaption support
* Fix to using CKEditro in inlines


Install
=======

::

    $ pip install django_ckeditor_improved

Example
-------


#settings.py
1. Image picker set up at /admin/media/imagepicker/
2. Custom ckeditor css file loaded from /static/admin/ckeditor.css

    CKEDITOR_BASIC = {
        'filebrowserImageBrowseUrl': '/admin/media/imagepicker/',
        'filebrowserImageWindowWidth': '640',
        'filebrowserImageWindowHeight': '480',
        'height': '400px',
        'toolbar': [
            {
                'name': 'styles',
                'items': ['Format']
            },
            {
                'name': 'basicstyles',
                'items': ['Bold','Italic','Underline','Strike','Subscript','Superscript']
            },
            {
                'name': 'paragraph',
                'groups': ['list'],
                'items': ['NumberedList', 'BulletedList', 'Blockquote']
            },
            {
                'name': 'media',
                'items': ['Image', 'CreateDiv']
            },
            {
                'name': 'links',
                'items': ['Link', 'Unlink', 'Anchor']
            },
            {
                'name': 'insert',
                'items': ['HorizontalRule', 'PageBreak', 'SpecialChar', 'Table', 'Iframe', 'Image']
            },
            {
                'name': 'pasting',
                'items': ['PasteText', 'PasteFromWord', 'RemoveFormat']
            },
            {
                'name': 'tools',
                'items': ['Maximize']
            },
            {
                'name': 'source',
                'items': ['Source']
            }       
        ],
        'allowedContent' : 
            'h1 h2 h3 p blockquote strong em sup u;'\
            'ol ul li;'\
            'figure{width,height,display,float};'\
            'figcaption{width,height,display,float,text-align,margin};'\
            'img[!src,alt,width,height,align,data-caption,style]{display,margin,float};'\
            'div(*);',
        'removeButtons' : '',
        'forcePasteAsPlainText' : 'true',
        'contentsCss': STATIC_URL + 'admin/ckeditor.css',
    }


#admin.py
    class PageAdmin(admin.ModelAdmin):
        form = PageForm


#forms.py
    class PageForm(forms.ModelForm):
        class Meta:
            model = Page
            widgets = {
                'content': CKEditorWidget(config=settings.CKEDITOR_BASIC)
            }


See https://github.com/espenak/django_ckeditorfiles for further setup and configuration instructions