#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
    flask_cache._compat
    ~~~~~~~~~~~~~~~~~~~

    Some py2/py3 compatibility support based on a stripped down
    version of six so we don't have to depend on a specific version
    of it.

    :copyright: (c) 2013 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import sys

PY2 = sys.version_info[0] == 2
PYPY = hasattr(sys, 'pypy_translation_info')


if not PY2:
    text_type = str
    string_types = (str,)
    range_type = range

    iterkeys = lambda d: iter(list(d.keys()))
    itervalues = lambda d: iter(list(d.values()))
    iteritems = lambda d: iter(list(d.items()))

    import pickle
    from io import BytesIO, StringIO
    NativeStringIO = StringIO

else:
    text_type = str
    string_types = (str, str)
    range_type = xrange

    iterkeys = lambda d: iter(list(d.keys()))
    itervalues = lambda d: iter(list(d.values()))
    iteritems = lambda d: iter(list(d.items()))

    import pickle as pickle
    from io import StringIO as BytesIO, StringIO
    NativeStringIO = BytesIO
