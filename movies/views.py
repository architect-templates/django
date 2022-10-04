
from http.client import HTTPResponse
from django.http import JsonResponse
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Movie

def error_check(name, rating):
    if not name:
      return 'Please provide a movie name'
    elif not rating:
      return 'Please provide a rating'
    elif int(rating) < 1 or int(rating) > 5:
      return'Please provide a rating between 1-5'
    else:
      return None

@method_decorator(csrf_exempt, name='dispatch')
def home(request):
  if request.method == 'POST':
    # Parse out data
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    name = body['name']
    rating = body['rating']

    # check data
    err = error_check(name, rating)
    if err:
      messages.error(request,err)
      return HTTPResponse('<h1>' + err + '</h1>')
    
    data = Movie(name=name, rating=rating)
    data.save()

  movie_data = Movie.objects.all().values()
  out_data = list(movie_data)
  print(out_data)
  return JsonResponse(out_data, safe=False)
