from django.conf.urls import patterns, url

from diary.views import *

urlpatterns = patterns('',
    url(r'^view/([a-zA-Z]+)$', view_contact),
    url(r'^view/$', view_all),
    url(r'^add/$', add),
    url(r'^create$', create),
)