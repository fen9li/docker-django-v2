# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from home.models import Movie

class MovieList(ListView):
    model = Movie
