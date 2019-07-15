from django.contrib import admin

# Register your models here.

from home.models import Movie
admin.site.register(Movie)

from home.models import Person
admin.site.register(Person)
