#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView
from webpage.models import *


class HomeView(TemplateView):
    template_name = "landing.html"


class RessortDetailView(DetailView):
    context_object_name = "ressort"
    template_name = "ressort.html"
    model = Ressort

    # def get_context_data(self, **kwargs):
    #     context = super(RessortDetailView, self).get_context_data(**kwargs)
    #     return context


class ArticleDetailView(DetailView):
    context_object_name = "article"
    template_name = "article.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['text'] = self.object.get_body()
        context['specwords'] = self.object.get_specwords()
        return context


class AboutUsView(TemplateView):
    template_name = "aboutus.html"
