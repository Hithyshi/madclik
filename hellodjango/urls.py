from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'zone.views.homepage', name='homepage'),
    url(r'^zone/postad/$', 'zone.views.postadv', name='postadv'),
    url(r'^zone/search/$', 'zone.views.homesearch', name='homesearch'),
    url(r'^zone/catg/$', 'zone.views.homecatg', name='homecatg'),
    url(r'^zone/secsearch/$', 'zone.views.secsearch', name='secsearch'),
    url(r'^zone/postsuccess/$', 'zone.views.postsuccess', name='postsuccess'),
    url(r'^zone/catg/(?P<item_cat>[^/]+)/$', 'zone.views.searchcaticon', name='searchcaticon'),
    url(r'^zone/product/(?P<product_title>[^/]+)/(?P<product_id>[^/]+)/$', 'zone.views.productdisplay', name='productdisplay'),
    url(r'^zone/search/(?P<search_txt>[^/]+)/filter/$', 'zone.views.searchfilter', name='searchfilter'),
    url(r'^zone/search/(?P<search_txt>[^/]+)/loca/$', 'zone.views.searchloca', name='searchloca'),
    url(r'^zone/search/(?P<search_txt>[^/]+)/(?P<filter_radio>[^/]+)/loca/$', 'zone.views.searchradloca', name='searchradloca'),
    url(r'^zone/search/(?P<search_txt>[^/]+)/(?P<filter_loca>[^/]+)/filter/$', 'zone.views.searchlocrad', name='searchlocrad'),
    url(r'^zone/search/(?P<search_txt>[^/]+)//filter/$', 'zone.views.noloca', name='noloca'),
    url(r'^zone/catg/(?P<search_catg>[^/]+)/filter/$', 'zone.views.catgfilter', name='catgfilter'),
    url(r'^zone/catg/(?P<search_catg>[^/]+)/loca/$', 'zone.views.catgloca', name='catgloca'),
    url(r'^zone/catg/(?P<search_catg>[^/]+)/(?P<filter_radio>[^/]+)/loca/$', 'zone.views.catgradloca', name='catgradloca'),
    url(r'^zone/catg/(?P<search_catg>[^/]+)/(?P<filter_loca>[^/]+)/filter/$', 'zone.views.catglocrad', name='catglocrad'),
    url(r'^zone/catg/(?P<search_catg>[^/]+)//filter/$', 'zone.views.catgnoloca', name='catgnoloca'),
    url(r'^zone/reachus/$', 'zone.views.reachus', name='reachus'),
    url(r'^zone/termsofuse/$', 'zone.views.termsofuse', name='termsofuse'),
    #url(r'^zone/search/testing/$', 'zone.views.iframetesting', name='iframetesting'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
