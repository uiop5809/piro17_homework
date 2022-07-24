from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
  path('', views.comment_list, name="comment_list"),
  path('like_ajax/', views.like_ajax, name="like_ajax"),
  path('delete_ajax/', views.delete_ajax, name="delete_ajax"),
]