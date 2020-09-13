from django.urls import path

from core.models import Genre, Movie

from core.views import MovieCreateView

from core.views import MovieUpdateView

from core.views import MovieDeleteView

from core.views import MovieListView

from core.views import MovieDetailView

app_name = 'core'

urlpatterns = [
    # path('', MovieView.as_view(), name='index'),
    path('movie/list', MovieListView.as_view(), name='movie_list'),
    path('movie/detail/<pk>', MovieDetailView.as_view(), name='movie_detalis'),
    path('movie/create', MovieCreateView.as_view(), name='movie_create'),
    path('movie/update/<pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<pk>', MovieDeleteView.as_view(), name='movie_delete'),
    # path('', movies, name="index")
]
