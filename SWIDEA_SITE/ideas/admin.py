from django.contrib import admin
from .models import Idea

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
  pass
