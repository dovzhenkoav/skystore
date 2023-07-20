from django.contrib import admin

from app_blog.models import BlogPost
# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'is_published', 'view_count')
    list_filter = ('is_published', 'view_count')
    search_fields = ('name',)
