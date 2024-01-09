"""
WSGI config for aviator_game project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""
import os
import sys
import platform

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aviator_game.settings")
sys.path.insert(0,'/home/c/cw15060/az/public_html/aviator_game')
sys.path.insert(0,'/home/c/cw15060/venv/lib/python{0}/site-packages'.format(platform.python_version()[0:31]))



from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()