
from django.http import JsonResponse


def home(request):
  return JsonResponse({'foo':'bar'})
