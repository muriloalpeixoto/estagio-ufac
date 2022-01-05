#estagio/main/apps.py
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

import environ
import os

#app.config['MAIL_AUTH'] = ['PLAIN', 'LOGIN', 'CRAM-MD5']

class MainConfig(AppConfig):
    name = "estagio.main"
    verbose_name = _("Main")

    def ready(self):
        try:
            pass
        except ImportError:
            pass