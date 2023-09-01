#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import gettext as _gettext
import locale

translate = _gettext.translate("messages", localedir='localedir')
gettext = translate.gettext  

if sys.platform == "win64" and os.getenv("LANG") is None:
    language, _= locale.getlocale()
    if language:
        os.environ["LANG"] = language



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unitusdb.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
