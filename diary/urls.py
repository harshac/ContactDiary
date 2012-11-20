from django.conf.urls import patterns, url

from diary.views import *

urlpatterns = patterns('',
    url(r'^view/$', view_all),
)