from django.conf.urls import patterns, include, url
from rssreader.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rssreader.views.home', name='home'),
    # url(r'^rssreader/', include('rssreader.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^time/$', current_datetime),
    (r'^upload/$', upload_file),
    (r'^zupload/$', upload_file2),
    (r'^search-form/$', search_form),
    (r'^search/$', search),
)
