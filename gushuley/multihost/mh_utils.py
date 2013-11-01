import re
from threading import currentThread
from django.conf import settings
import django.contrib
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponsePermanentRedirect
from django.utils.cache import patch_vary_headers
from gushuley.multihost import models

__author__ = 'andriy'

_sites = {}
_default_site = None


def get_current_site():
    if currentThread() in _sites:
        return _sites[currentThread()]
    return None


def mh_reverse(name, site, is_external=False, args=None, kwargs=None):
    if not site:
        site = _default_site

    if is_external or get_current_site() != site:
        return site.site.domain + reverse(name, urlconf=site.urls_module, args=args, kwargs=kwargs)
    else:
        return reverse(name, urlconf=site.urls_module, args=args, kwargs=kwargs)


class MultiHostMiddleware:
    def __init__(self):
        pass

    def process_request(self, request):
        global  _default_site
        if not _default_site:
            _default_site = models.Site()
            _default_site.site = django.contrib.sites.models.Site.objects.get(id=settings.SITE_ID)
            _default_site.urls_module = settings.ROOT_URLCONF

        _host = request.META["HTTP_HOST"]
        site = None
        for host in models.Site.objects.order_by("order").all():
            r = re.compile(host.host_regexp)
            if r.match(_host):
                if host.urls_module:
                    setattr(request, "urlconf", host.urls_module)
                else:
                    if hasattr(request, "urlconf"):
                        delattr(request, "urlconf")
                site = host
                break
            elif _host.startswith("www.") and r.match(_host[4:]):
                path = u'%s%s' % (host.site.domain, request.META["PATH_INFO"],)
                if request.META["QUERY_STRING"]:
                    path = u'%s?%s' % (path, request.META["QUERY_STRING"], )
                return HttpResponsePermanentRedirect(path)

        if not site:
            try:
                site = models.Site.objects.get(site__id__exact=settings.SITE_ID)
            except ObjectDoesNotExist:
                site = _default_site
        _sites[currentThread()] = site

    def process_response(self, request, response):
        patch_vary_headers(response, ('Host',))
        return response