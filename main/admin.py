from django.contrib import admin
from main.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'updated_at', 'created_at', 'id']
    list_filter = ['created_at']
    search_fields = ['id', 'title']
    readonly_fields = ['created_at', 'updated_at']
