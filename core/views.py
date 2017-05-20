# coding=utf-8
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView


# Página inicial
class IndexView(TemplateView):
    #context_object_name = 'noticias_destaque'
    #queryset = Noticia.objects.filter(~Q(image='')).order_by('-published_at')[0:4]
    template_name = 'index.html'
