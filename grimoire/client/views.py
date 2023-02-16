from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse

# Create your views here.

@api_view(['GET',])
def temporary(request):
    return HttpResponse('<h1>Hello</h1>')