import logging
import os
import sys
from django.core.wsgi import get_wsgi_application
from django.conf import settings

import pymysql
pymysql.install_as_MySQLdb()

# Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_conf.settings")
sys.stdout = sys.stderr

DEBUG = False

application = get_wsgi_application()
