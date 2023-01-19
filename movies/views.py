from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import View, generic

from .models import Movie


class BaseView(View):
  def get(self, request):
    return HomeView.as_view()(request)

class HomeView(generic.ListView):
  template_name = 'movies/movies.html'
  context_object_name = 'movies'

  def get_queryset(self):
    return Movie.objects.all()

  def post(self, request):
    # Data Cleanse
    name = request.POST['movie_name']
    rating = request.POST['movie_rating']

    err = error_check(name, rating)
    if err:
      messages.error(request,err)
      return HttpResponseRedirect('/')
    else:
      data = Movie(name=name, rating=rating)
      data.save()
      return HttpResponseRedirect('/')

def error_check(name, rating):
  if not name:
    return 'Please provide a movie name'
  elif not rating:
    return 'Please provide a rating'
  elif int(rating) < 1 or int(rating) > 5:
    return'Please provide a rating between 1-5'
  else:
    return None
