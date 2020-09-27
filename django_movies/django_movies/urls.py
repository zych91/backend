"""django_movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.models import Genre, Movie
from core.views import hello

from core.views import MovieCreateView

from core.views import MovieUpdateView

from core.views import MovieDeleteView

from .views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path("core/", include("core.urls", namespace='core')),
    path('', IndexView.as_view(), name="index"),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
