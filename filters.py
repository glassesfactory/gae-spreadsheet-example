# -*- coding: utf-8 -*-

"""
see:
http://kay-snippets.appspot.com/snippets/198001
"""

from jinja2 import environmentfilter

@environmentfilter
def mb_truncate(environment, value, length=100, end='...'):
    if len(value) < length:
        return value
    else:
        return value[:length] + end