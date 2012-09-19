#!/usr/bin/env python
from django.core.management import call_command
import os

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    with open('server.pid', 'w') as fobj:
        fobj.write(str(os.getpid()))
    try:
        call_command('runserver', '127.0.0.1:8888', use_threading=True)
    finally:
        os.remove('server.pid')
