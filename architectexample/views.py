
from django.http import HttpResponse


def home(request):
  return HttpResponse("<H1>Architect Movie App</H1>")
