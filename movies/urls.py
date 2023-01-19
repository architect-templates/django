from django.urls import include, path

from . import views

app_name = 'movies'

urlpatterns = [
  path('', views.HomeView.as_view(), name='home')
]
