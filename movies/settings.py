"""
Django settings for django project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/

"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import os

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

SECRET_KEY = os.environ.get('SECRET_KEY', 'warning-override-for-production')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['localhost', '0.0.0.0', 'https://app.localhost.architect.sh', os.environ.get('ALLOWED_HOST', '')]

CSRF_TRUSTED_ORIGINS = ['https://*.localhost.architect.sh/','https://*.127.0.0.1']

USE_X_FORWARDED_HOST = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ROOT_URLCONF = 'movies.urls'

WSGI_APPLICATION = 'movies.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ.get('POSTGRES_DB', 'postgres'),
    'USER': os.environ.get('POSTGRES_USER', 'postgres'),
    'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
    'HOST': os.environ.get('POSTGRES_HOST', '0.0.0.0'),
    'PORT': os.environ.get('POSTGRES_PORT', '5432'),
  }
}

INSTALLED_APPS = [
  'movies.apps.MoviesConfig',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles'
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [ BASE_DIR / 'templates' ],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
      ],
    },
  },
]

