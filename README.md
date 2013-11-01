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

    {{http[s]://site-name.org}}

In your code:

{{from gushuley.multihost import mh_reverse, get_current_site}}

You can build urls for different sites with a full url.

{{mh_reverse(news_item, site=None, full_url=False, [site.two_letter_code, nid])}} - build short url for default site - /BB/news/item/XXX/}}
{{mh_reverse(news_item, site=None, full_url=False, [site.two_letter_code, nid])}} - build full url for default site - http://default.site/BB/news/item/XXX/}}
{{mh_reverse(news_item, site=mobile, full_url=False, [site.two_letter_code, nid])}} - build full url for separate site - http://mobile.site/BB/ni/XXX/}}
