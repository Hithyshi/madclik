from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^zone/$', 'zone.views.homepage', name='homepage'),
    url(r'^zone/postad/$', 'zone.views.postadv', name='postadv'),
    url(r'^zone/search/$', 'zone.views.homesearch', name='homesearch'),
    url(r'^zone/postsuccess/$', 'zone.views.postsuccess', name='postsuccess'),
    url(r'^zone/search/filter/$', 'zone.views.searchfilter', name='searchfilter'),
    #url(r'^zone/search/testing/$', 'zone.views.iframetesting', name='iframetesting'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
