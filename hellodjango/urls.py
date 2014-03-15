from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^zone/$', 'zone.views.homepage', name='homepage'),
    url(r'^zone/search/$', 'zone.views.homesearch', name='homesearch'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
