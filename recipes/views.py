from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/pages/home.html',
                  context={
                      'name': 'Carlos',
                      'age': 25,
                      'is_published': True,
                  })

def recipe(request):
    return render(request, 'recipes/pages/home.html',
                  context={
                      'name': 'Carlos',
                      'age': 25,
                      'is_published': True,
                  })
