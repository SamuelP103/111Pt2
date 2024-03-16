from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModeAdmin):
    list_display = ['title', 'subtitle', 'body']

admin.site.register(Post, PostAdmin)


