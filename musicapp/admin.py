from django.contrib import admin

from .models import Artiste, Song, Lyric
admin.site.register(Artiste)
admin.site.register(Lyric)
admin.site.register(Song)