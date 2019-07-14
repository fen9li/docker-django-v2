from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('movies/', views.MovieList.as_view(), name='MovieList'),
]
