from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello World, You're at the polls index")

def detail(request, question_id):
    response = f"You're looking at question {question_id}."
    return HttpResponse(response)

def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)

def vote(request, question_id):
    response = f"You're voting on question {question_id}."
    return HttpResponse(response)
