"""Hackdays15 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from webpage.views import *
from webpage.models import *

admin.site.register(Ressort)
admin.site.register(Article)

base_name = "dev"


urlpatterns = [
    url(r'^{}/admin/'.format(base_name), include(admin.site.urls)),
    url(r'^{}/$'.format(base_name), HomeView.as_view(), name="landing"),
    url(r'^{}/contact/$'.format(base_name), AboutUsView.as_view(), name="aboutus"),
    url(r'^{}/(?P<slug>[^/]+)/$'.format(base_name), RessortDetailView.as_view(), name="ressort"),
    url(r'^{}/(?P<ressort>[^/]+)/(?P<slug>.+)/$'.format(base_name), ArticleDetailView.as_view(), name="article"),

]
