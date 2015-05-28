#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'speredenn'
SITENAME = u'Carnets de route'
SITEURL = 'https://speredenn.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Tails', 'https://tails.boum.org/'),
         ('GNUPG', 'https://www.gnupg.org/'),
         ('Tor', 'https://www.torproject.org/'),
         ('Git', 'http://git-scm.com/about/'),
         ('Mercurial', 'http://mercurial.selenic.com/'),
         ('Mozilla', 'http://www.mozilla.org/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/speredenn'),
          ('Twitter', 'https://www.twitter.com/speredenn'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme stuff

THEME = "notmyidea"

# Other stuff

GITHUB_URL = "https://github.com/speredenn/speredenn.github.io"
DISQUS_SITENAME = "speredenn-notebook"
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
