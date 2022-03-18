
from django.http import HttpResponse


def home(request):
  return HttpResponse("<H1>Welcome to the Polls app!</H1><H2>Navigate to /polls or /admin to get started</H2>")
