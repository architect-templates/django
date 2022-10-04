from django.urls import path, include

from . import views

app_name = 'movies'

urlpatterns = [
  path('', views.home, name='home')
]
