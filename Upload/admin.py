from django.contrib import admin
from .models import Uploads,PostImages

# Register your models here.


class FeedFileInline(admin.TabularInline):
    model = PostImages


class FeedAdmin(admin.ModelAdmin):
    inlines = [
        FeedFileInline,
    ]

admin.site.register(Uploads)
admin.site.register(PostImages)



