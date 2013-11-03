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
        # should be called after FetchFromCacheMiddleware
        'gushuley.multihost.mh_utils.MultiHostMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
        )

Setup you'r multihost sites objects.

Standard core django sites host names should be configured to actual accesible domain names with protocol name and port values without ending slash:

    https://site-name.org:8433

In your code:

    from gushuley.multihost import mh_utils

Yu can query current site, which serves a request:

    mh_utils.get_current_site.site # link to django site object

You can build urls for different sites with a full url.

    mh_utils.mh_reverse(news_item, site=None, full_url=False, [site.two_letter_code, nid])

Build short url for default site - /BB/news/item/XXX/

    mh_utils.mh_reverse(news_item, site=None, full_url=False, [site.two_letter_code, nid])

Build full url for default site - http://default.site/BB/news/item/XXX/

    mh_utils.mh_reverse(news_item, site=mobile, full_url=False, [site.two_letter_code, nid])

Build full url for separate site - http://mobile.site/BB/ni/XXX/

The same is from django templates:

    {% import multihost %}

    {% mh_reverse 'portal-news-item' '' 'pb' %}
    {% mh_reverse 'portal-news-item' 'mobile' 'pb' %}

License (and related information):
===
Originally written by Andriy Gushuley.

This program is licensed under the MIT License (see LICENSE.txt)