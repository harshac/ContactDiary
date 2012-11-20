from django.conf.urls import patterns, url

from diary.views import *

urlpatterns = patterns('',
    url(r'^view/$', view_all),
    url(r'^view/([a-zA-Z]+)$', view_contact),
)