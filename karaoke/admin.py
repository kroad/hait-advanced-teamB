from django.contrib import admin

from .models import Scale, Artist, Song, Voice, UserScale

admin.site.register(Scale)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Voice)
admin.site.register(UserScale)