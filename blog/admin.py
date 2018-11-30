from django.contrib import admin
from .models import BlogType,Blog
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','blog_type','get_read_num','content','author','created_time','last_update_time')
# @admin.register(ReadNum)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('read_num','blog')


