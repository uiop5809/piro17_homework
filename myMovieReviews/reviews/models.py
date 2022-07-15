from django.db import models

# Create your models here.
class Review(models.Model):
  GENRE_CHOICE = (
    ('default', '----------'),
    ('액션', 'Action'),
    ('코미디', 'Comedy'),
    ('범죄', 'Crime'),
    ('판타지', 'Fantasy'),
    ('공포', 'Horror'),
    ('로맨스', 'Romance'),
    ('공상과학', 'SF'),
  )

  title = models.CharField(max_length= 100, verbose_name="제목")
  year = models.CharField(max_length= 50, verbose_name="개봉년도")
  genre = models.CharField(max_length= 50, choices = GENRE_CHOICE, verbose_name="장르")
  grade = models.DecimalField(max_digits=10, decimal_places=1, verbose_name="별점")
  time = models.IntegerField(verbose_name="러닝타임")
  review = models.TextField(verbose_name="리뷰")
  director = models.CharField(max_length= 50, verbose_name="감독")
  actor = models.CharField(max_length= 50, verbose_name="배우")

