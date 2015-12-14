

from django.conf.urls import include, url,patterns
from django.contrib import admin
from homework_1_cs361 import views



urlpatterns = [

    url(r'^histogram/(?P<dosya>.*)/$', views.counting),

]

