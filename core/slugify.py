from __future__ import unicode_literals

import re
from unicodedata import normalize

re_script = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(string, delimeter='-'):
    result = []
    for word in re_script.split(string.lower()):
        if word:
            result.append(word)
    return str(delimeter.join(result))