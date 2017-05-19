# -*- coding: UTF-8 -*-
from django.db import models
from django.conf import settings


class Album(models.Model):

    ''' Album de fotografias '''

    name = models.CharField(u'Título do album', max_length=300)
    slug = models.SlugField(editable=False)
    description = models.CharField(u'Descrição do album', max_length=300, null=True, blank=True)
    date_created = models.DateTimeField('Criado em', auto_now_add=True)
    date_modified = models.DateTimeField('Modificado em', auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albuns'
        ordering = ['name']

    def __str__(self):
        return self.name


class Photo(models.Model):

    ''' Modelo para fotos '''

    title = models.CharField(u'Título', max_length=300)
    legend = models.TextField('Legenda', blank=True, null=True)
    date_created = models.DateTimeField('Criado em', auto_now_add=True)
    date_modified = models.DateTimeField('Modificado em', auto_now=True)
    image = models.ImageField(upload_to='fotos/%Y/%m')
    album = models.ForeignKey(Album, verbose_name='Album', related_name='fotos')
    photographer = models.CharField('Nome do Fotografo', max_length=200, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Criado por', editable=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['title']

    def __str__(self):
        return self.title