# from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView, DetailView,
)
from home.models import Movie, Person

class MovieDetail(DetailView):
    queryset = Movie.objects.all_with_related_persons()

class MovieList(ListView):
    model = Movie
    paginate_by = 10

class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()

class PersonList(ListView):
    model = Person
    paginate_by = 10