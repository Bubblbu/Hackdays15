#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView
from webpage.models import *


class HomeView(ListView):
    model = Article
    context_object_name = "article_list"
    template_name = "landing.html"
    # paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['article_list'] = Article.objects.exclude(ressort=Ressort.objects.filter(slug="schwerpunkt"))
        context['schwerpunkt_list'] = Article.objects.filter(ressort=Ressort.objects.filter(slug="schwerpunkt"))
        return context


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
        context['descs'] = Description.objects.all()
        return context


class AboutUsView(TemplateView):
    template_name = "aboutus.html"


class CategoryBaseView(ListView):
    model = Category
    template_name = "cat_base.html"
    context_object_name = "category_list"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "cat_detail.html"
    context_object_name = "cat"

    # def get_context_data(self, **kwargs):
    #     context = super(LexikonListView, self).get_context_data(**kwargs)
    #     context['text'] = self.object.get_body()
    #     context['specwords'] = self.object.get_specwords()
    #     return context


class DescDetailView(DetailView):
    model = Description
    template_name = "desc_detail.html"
    context_object_name = "desc"

    # def get_context_data(self, **kwargs):
    #     context = super(LexikonListView, self).get_context_data(**kwargs)
    #     context['text'] = self.object.get_body()
    #     context['specwords'] = self.object.get_specwords()
    #     return context
