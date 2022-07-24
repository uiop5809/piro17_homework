from django.db import models

class Comment(models.Model):
  name = models.CharField(default="user_name", blank=True, null=False, max_length=50, verbose_name="이름")
  content = models.TextField(blank=True, max_length=500, verbose_name="내용")
  like = models.BooleanField(default=False, verbose_name="좋아요")
