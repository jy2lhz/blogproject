from django.contrib import admin
from .models import Post, Category, Tag
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    summernote_fields = ('body',)  # 给content字段添加富文本

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)