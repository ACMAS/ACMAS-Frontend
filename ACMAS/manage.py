#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import random
import string
import base64
import hashlib


#ID = tCOlKcXw0cRmLjH4MV34voHrmoliuTdl1E7EjJ4s
#SECRET = N9OkuslGhOMZluXt2cMWQsTVYxXIJ0h3DUGtNbBP0cxFxhU8KOGAcztrmMQ50X2KGgrN5wl2yiYeqD7BXCSYV5oG1RdjhEjLksQy79fkqGcYsSzjjAd17vpCWrYQLvmw

code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))
code_verifier = base64.urlsafe_b64encode(code_verifier.encode('utf-8'))

code_challenge = hashlib.sha256(code_verifier).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')



def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ACMAS.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
