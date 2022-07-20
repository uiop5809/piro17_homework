from django.db import models
from django.contrib.auth.models import User

class Tool(models.Model):
  name = models.CharField(max_length=100, verbose_name="이름")
  kind = models.CharField(max_length=100, verbose_name="종류")
  content = models.TextField(max_length=100, verbose_name="내용")

class Idea(models.Model):
  title = models.CharField(max_length=100, verbose_name="제목")
  image = models.ImageField(blank=True, upload_to='ideas/%Y%m%d', verbose_name="사진")
  content = models.TextField(verbose_name="설명")
  interest = models.IntegerField(verbose_name="관심도")
  devtool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name="dev_tool", verbose_name="개발툴")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")
  like = models.ManyToManyField(User, related_name="likes", blank="True", verbose_name="찜하기")
