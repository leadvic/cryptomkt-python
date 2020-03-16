# coding: utf-8
import six
if six.PY2:
  from itertools import imap
  from urllib import quote
  from urllib import unquote
  from urllib import urlencode
  from urlparse import urljoin
  from urlparse import urlparse
elif six.PY3:
  imap = map
  from urllib.parse import unquote
  from urllib.parse import quote
  from urllib.parse import urljoin
  from urllib.parse import urlparse
  from urllib.parse import urlencode