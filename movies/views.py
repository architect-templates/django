
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib import messages

from .models import Movie

class BaseView(View):
  def get(self, request):
    return HomeView.as_view()(request)

  def post(self, request):
    # Data Cleanse
    name = request.POST['formName']
    rating = request.POST['forRating']

    err = error_check(name, rating)
    if err:
      messages.error(request,err)
      return HttpResponseRedirect('/movies/')
    else:
      data = Movie(name=name, rating=rating)
      data.save()
      return HttpResponseRedirect('/movies/')

class HomeView(generic.ListView):
  template_name = 'movies/movies.html'
  context_object_name = 'movies_exist'

  def get_queryset(self):
    return Movie.objects.all()

def error_check(name, rating):
    if not name:
      return 'Please provide a movie name'
    elif not rating:
      return 'Please provide a rating'
    elif int(rating) < 1 or int(rating) > 5:
      return'Please provide a rating between 1-5'
    else:
      return None
