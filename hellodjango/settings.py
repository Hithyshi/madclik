"""
Django settings for hellodjango project.


For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rq7-5w2#($uo#r#s86pbyk4v)kysgffdkspy^!ln*hlgt7_m+s'
ACCESS_KEY = 'AKIAJH3OOHCZTBK2MK2A'
PASS_KEY = 'MEs5DcP4VuU+LTAe7HGEfOSAfbAGTDKiZOwDWeHr'
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'info@madclik.com'
EMAIL_HOST_PASSWORD = 'rent-estu'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_evolution',
    'zone',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hellodjango.urls'

WSGI_APPLICATION = 'hellodjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'test',
        'USER':'tutorialuser',
        'PASSWORD':'tutorialuser',
        'HOST':'',
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'heroku_ca7984bc0fbd92a',
        'USER':'be1bed63bcc02c',
        'PASSWORD':'01358f51',
        'HOST':'us-cdbr-east-05.cleardb.net',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Parse database configuration from $DATABASE_URL
import dj_database_url
#DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

import os
import sys
import urlparse


# db for heroku
# Register database schemes in URLs.
urlparse.uses_netloc.append('mysql')

try:

    # Check to make sure DATABASES is set in settings.py file.
    # If not default to {}

    if 'DATABASES' not in locals():
        DATABASES = {}

    if 'DATABASE_URL' in os.environ:
        url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])

        # Ensure default database exists.
        DATABASES['default'] = DATABASES.get('default', {})

        # Update with environment configuration.
        DATABASES['default'].update({
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
        })


        if url.scheme == 'mysql':
            DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
except Exception:
    print 'Unexpected error:', sys.exc_info()
