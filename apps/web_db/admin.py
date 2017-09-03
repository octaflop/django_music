from django.contrib import admin

from web_db import models


class SongAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class SongInline(admin.TabularInline):
    model = models.Song


class AlbumAdmin(admin.ModelAdmin):
    search_fields = ('title', 'artist', 'year',)
    inlines = (SongInline,)

admin.site.register(models.Album, AlbumAdmin)
admin.site.register(models.Song, SongAdmin)
