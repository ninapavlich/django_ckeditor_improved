import os
import sys

from django.conf.global_settings import *   # pylint: disable=W0614,W0401

import apps as project_module

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1
TIME_ZONE = 'UTC'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)

GRAPPELLI_ADMIN_TITLE = "C&G Partners | Example"
GRAPPELLI_INDEX_DASHBOARD = 'example.dashboard.ExampleDashboard'

#==============================================================================
# Apps
#==============================================================================

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',

    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',

    'example.apps.items',
    'example.apps.media',

    'ckeditor',
    'imagekit',
    'reversion',
    'south',
    'south',
    'storages',
)

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================

APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir))
DATA_DIR = os.path.join(APP_DIR, 'data')
PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))
PYTHON_BIN = os.path.dirname(sys.executable)
ve_path = os.path.dirname(os.path.dirname(os.path.dirname(PROJECT_DIR)))

if os.path.exists(os.path.join(PYTHON_BIN, 'activate_this.py')):
    VAR_ROOT = os.path.join(os.path.dirname(PYTHON_BIN), 'var')
elif ve_path and os.path.exists(os.path.join(ve_path, 'bin',
        'activate_this.py')):
    VAR_ROOT = os.path.join(ve_path, 'var')
else:
    VAR_ROOT = os.path.join(PROJECT_DIR, 'var')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

#==============================================================================
# Project URLS and Media Settings
#==============================================================================

ROOT_URLCONF = 'example.urls'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')


STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR,  '..', 'static'),
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)


#==============================================================================
# DATABASES
#==============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'django_ckeditorfiles_4_3',
    }
}

#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, '..', 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
    "django.core.context_processors.request",
)


#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

#==============================================================================
# Auth / security
#==============================================================================

ACCOUNT_ACTIVATION_DAYS = 7


AUTHENTICATION_BACKENDS += (
)

SECRET_KEY = 'cj51h)g!+qi-=&#ul0d+a8fdlakjhr3y4982orn238(*&(*&(*78687'


#==============================================================================
# App Settings
#==============================================================================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


#==============================================================================
# SEARCH Settings
#==============================================================================
CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, 'upload')
CKEDITOR_TOOLBAR = {
    'skin': 'moono',
    'toolbar_Basic': [
        ['Source', '-', 'Bold', 'Italic']
    ],
    'toolbar_Full': [
        ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
        ['Image', 'Flash', 'Table', 'HorizontalRule'],
        ['TextColor', 'BGColor'],
        ['Smiley', 'SpecialChar'], ['Source'],
    ],
    'toolbar': 'Full',
    'height': 291,
    'width': 835,
    'filebrowserWindowWidth': 940,
    'filebrowserWindowHeight': 725,
}