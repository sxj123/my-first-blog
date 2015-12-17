#from __future__ import unicode_literals
#coding=utf-8
from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):  #models.Model表明Post是一个django模型，所以django知道它应该被保存在数据库中
	author=models.ForeignKey('auth.user')#models.Foreignkey是指向另一个模型的链接
	title=models.CharField(max_length=200)#models.CharField这是你如何用为数有限的字符来定义一个文本
	text=models.TextField()#这是没有长度限制的常文本，可以添加博客的内容
	created_date=models.DateTimeField(default=timezone.now)#models.DateTimeField这是日期和时间
	published_date=models.DateTimeField(blank=True,null=True)#上面这几个都是属性

	def publish(self):#这是方法
		self.published_date=timezone.now()
		self.save()

	def __str__(self):  #调用__str__(),将得到文章标题的文本
		return self.title
#此时。我们已经创建完模型，后面就需要将模型添加到数据库中，命令：python manage.py makemigrations blog,然后输入python manage.py migrate blog
