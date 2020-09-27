from django.contrib import admin
from django.urls import path
from core.models import Movie, Genre, Director, Country
from core.views import hello

from accounts.models import Profile

admin.site.register(Movie)

admin.site.register(Genre)

admin.site.register(Director)

admin.site.register(Country)

admin.site.register(Profile)

# Register your models here.
