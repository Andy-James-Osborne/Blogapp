from django.contrib import admin
from .models import Post, Category1, Category2, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Category1)
admin.site.register(Category2)
admin.site.register(Comment)