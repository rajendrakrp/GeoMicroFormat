from django.conf.urls.defaults import *
from geoparser import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microformat_parser.views.home', name='home'),
    # url(r'^microformat_parser/', include('microformat_parser.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    url(r'^geolinks/$', views.getlink, name="link"),
)
