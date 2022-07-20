from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ideas"

urlpatterns = [
  path("", views.IdeaHome, name="IdeaHome"),
  path("IdeaCreate", views.IdeaCreate, name="IdeaCreate"),
  path("IdeaDetail/<int:id>/", views.IdeaDetail, name="IdeaDetail"),
  path("IdeaUpdate/<int:id>/", views.IdeaUpdate, name="IdeaUpdate"),
  path("IdeaDelete/<int:id>/", views.IdeaDelete, name="IdeaDelete"),

  path("ToolHome", views.ToolHome, name="ToolHome"),
  path("ToolCreate", views.ToolCreate, name="ToolCreate"),
  path("ToolDetail/<int:id>/", views.ToolDetail, name="ToolDetail"),
  path("ToolUpdate/<int:id>/", views.ToolUpdate, name="ToolUpdate"),
  path("ToolDelete/<int:id>/", views.ToolDelete, name="ToolDelete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)