#coding=utf-8
#python
from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)#创建模型后，需要在admin中注册所创建的模型
