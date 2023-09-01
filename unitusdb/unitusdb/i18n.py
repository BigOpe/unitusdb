"""Internationalization (i18n) support.

Translate text in to your native language using the gettext() function.
"""

import gettext as _gettext
import importlib.resources
import locale
import os
import sys

if sys.platform == "win32" and os.getenv("LANG") is None:
    language, _ = locale.getlocale()
    if language:
        os.environ["LANG"] = language

try:
    localedir = importlib.resources.files("unitusdb") / "locale"
    translate = _gettext.translation("messages", localedir=str(localedir))
    gettext = translate.gettext

except OSError as e:
    print(f"No translations were found: {e}")

    def gettext(s):
        return s