# from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView, DetailView,
)
from home.models import Movie

class MovieDetail(DetailView):
    model = Movie

class MovieList(ListView):
    model = Movie
