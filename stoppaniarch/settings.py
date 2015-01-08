"""
Django settings for stoppaniarch project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
import sys
import signal
from functools import partial

import dj_database_url
from django.core.exceptions import ImproperlyConfigured


# Helpers

required = object()


def getenv(env, default=required, process=None):
    try:
        val = os.environ[env]
        return process(val) if process else val
    except KeyError:
        if default is required:
            raise ImproperlyConfigured(
                'Could not find the {} environment variable.'.format(env))
        return default

getbool = partial(getenv, process=lambda v: v.lower() in ('1', 'yes', 'true'))
getint = partial(getenv, process=int)
gettext = lambda s: s

if getbool('DOCKER', False):
    # Signal handler to trap SIGTERM signals sent by `docker stop` and
    # "gracefully" shutting down the server. Only installed when run inside
    # a docker container which explicitly sets the DOCKER environment
    # variable to 1.
    signal.signal(signal.SIGTERM, lambda _1, _2: sys.exit)


# Dynamic configuration

SECRET_KEY = getenv('SECRET_KEY')

DATA_DIR = getenv('DATA_DIR', os.path.dirname(os.path.dirname(__file__)))

DEBUG = getbool('DEBUG', False)
TEMPLATE_DEBUG = getbool('TEMPLATE_DEBUG', DEBUG)

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///project.db')
}

SITE_ID = getint('SITE_ID', 1)

TIME_ZONE = getenv('TIME_ZONE', 'Europe/Zurich')

ALLOWED_HOSTS = []


# Static configuration

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ROOT_URLCONF = 'stoppaniarch.urls'

WSGI_APPLICATION = 'stoppaniarch.wsgi.application'

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'stoppaniarch', 'static'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings'
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'stoppaniarch', 'templates'),
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'mptt',
    'menus',
    'sekizai',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_style',
    'djangocms_column',
    'djangocms_googlemap',
    'djangocms_inherit',
    'south',
    'reversion',
    'adminsortable',
    'parler',

    'stoppaniarch',
    'stoppaniarch.projects',
)

USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'it'

LANGUAGES = (
    ('it', gettext('italian')),
    ('de', gettext('german')),
    ('fr', gettext('french')),
    ('en', gettext('english')),
)

PARLER_LANGUAGES = {
    SITE_ID: [{'code': c[0]} for c in LANGUAGES],
    'default': {
        'fallback': LANGUAGE_CODE,
        'hide_untranslated': False,
    }
}

CMS_LANGUAGES = {
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'it',
            'hide_untranslated': False,
            'name': gettext('italian'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'de',
            'hide_untranslated': False,
            'name': gettext('german'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'fr',
            'hide_untranslated': False,
            'name': gettext('french'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('english'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ('fullwidth.html', gettext('Fullwidth')),
    ('sidebar_left.html', gettext('Sidebar Left')),
    ('sidebar_right.html', gettext('Sidebar Right')),
)

CMS_PERMISSION = False

CMS_PLACEHOLDER_CONF = {}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations'
}
