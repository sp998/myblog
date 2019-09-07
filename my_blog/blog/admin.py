from django.contrib import admin
from .models import Post
# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','author','datePosted')


admin.site.register(Post, PostsAdmin)


