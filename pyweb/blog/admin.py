from django.contrib import admin
from blog.models import BlogTable
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', '제목', '작성자', '수정일')

admin.site.register(BlogTable, BlogAdmin)
