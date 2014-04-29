from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.defaults import *
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns(
    "",
    (r'^$',  "articles.views.list_articles"),

    (r'^auth/', include('auth.urls')),
    (r'^articles/', include('articles.urls')),

    (r"^admin/", include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
