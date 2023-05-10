import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'users_RestAPI_React.settings')

application = get_wsgi_application()
