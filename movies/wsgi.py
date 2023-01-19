import os

from whitenoise import WhiteNoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movies.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root='/usr/src/app/static')
