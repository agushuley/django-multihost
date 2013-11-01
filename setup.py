#!/usr/bin/env python

# from distutils.core import setup
from setuptools import setup, find_packages
import metadata

app_name = metadata.name
version = metadata.version

setup(
    name = app_name,
    version = version,
    packages = find_packages(),
    include_package_data = True,
    author = "Andriy Gushuley",
    author_email = "agushuley@me.com",
    description = "A Django application/framework which allow to serve different hostnames "
                  "and urlconfs in one django application instance",
    long_description = \
"""
django-gu-multihost
===

**django-gu-multihost** is a Django application/framework which allow to serve different hostnames "
                  "and urlconfs in one django application instance
Quickstart:
===

Install django-gu-multihost:

    $ pip install django-gu-multihost

Add gu-multihost to INSTALLED_APPS in settings.py for your project:

    INSTALLED_APPS = (
        ...
        'gushuley.multihost',
    )

Add middleware class fetch from cache middleware :

    MIDDLEWARE_CLASSES += (
        'gushuley.multihost.MultiHostMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
        )

Setup you'r multihost sites objects.

Standard core django sites host names should be configured to actual values without ending /:

*http[s]://site-name.org*

In your code:

    from gushuley.multihost import mh_reverse, get_current_site

Yu can query current site, which serves a request:

    get_current_site.site # link to django site object

You can build urls for different sites with a full url.

    mh_reverse(news_item, site=None, full_url=False, [site.two_letter_code, nid])}}
        # build short url for default site - /BB/news/item/XXX/
    mh_reverse(news_item, site=None, full_url=False, [site.two_letter_code, nid])}}
        # build full url for default site - http://default.site/BB/news/item/XXX/}}
    mh_reverse(news_item, site=mobile, full_url=False, [site.two_letter_code, nid])}}
        # build full url for separate site - http://mobile.site/BB/ni/XXX/}}

The same is from django templates:

    {% import multihost %}

    {% mh_reverse 'portal-news-item' None 'pb' %}
    {% mh_reverse 'portal-news-item' 'mobile' 'pb' %}

License (and related information):
===
Originally written by Andriy Gushuley.

This program is licensed under the MIT License (see LICENSE.txt)
""",
    license = "MIT License",
    keywords = "django multihost framework",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms = ['any'],
    url = "https://github.com/agushuley/gu-multihost",
)