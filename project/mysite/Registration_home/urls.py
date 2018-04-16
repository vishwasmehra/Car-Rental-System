from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^login/',views.user),
    url(r'^Companylogin/', views.clog),
    url(r'^$', views.index),
]