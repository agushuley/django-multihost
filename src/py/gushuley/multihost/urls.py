#@PydevCodeAnalysisIgnore
from django.conf.urls.defaults import handler404, handler500, patterns,\
    url 
from django.conf import settings
import os.path
from django.http import HttpResponsePermanentRedirect
from gushuley.multihost import default_site

def redirect(req, path):
    return HttpResponsePermanentRedirect(u'%s/%s' % (default_site.site.domain, path,))

urlpatterns = patterns('',
     url(r'^(?P<path>.*)$', redirect),
)
