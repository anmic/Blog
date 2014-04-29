from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^register/$', "auth.views.register"),
                       (r'^login/$', "auth.views.login"),
                       (r'^logout/$', "auth.views.logout"),

)
