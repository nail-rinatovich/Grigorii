from django.contrib import admin
from .models import game, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(game, PostAdmin)