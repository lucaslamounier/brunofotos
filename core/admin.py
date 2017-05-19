# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Photo, Album


class PropertyImageInline(admin.StackedInline):
    model = Photo
    extra = 1


class AlbumAdmin(admin.ModelAdmin):

    list_display = ['name', 'author', 'date_created']
    search_fields = ['name']
    inlines = [PropertyImageInline, ]

    def save_model(self, request, obj, form, change):
        obj.slug = obj.name
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


admin.site.register(Album, AlbumAdmin)

