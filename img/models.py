#coding: utf8
from django.db import models

# Create your models here.
class Tu(models.Model):
    image = models.ImageField(u'图片', upload_to='uploads')
    name = models.CharField(u'名字', max_length=200)