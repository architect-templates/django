from django.urls import path, include

from . import views

app_name = 'movies'

urlpatterns = [
  path('', views.BaseView.as_view(), name='home')
]
