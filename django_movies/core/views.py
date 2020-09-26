from django.shortcuts import render
from django import views
from django.http import HttpResponse
from core.models import Movie
import logging
# Create your views here.

# def hello(request):
#   return HttpResponse("Hello World!")
from core.models import Genre
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView, DetailView

from core.forms import MovieForm

logging.basicConfig(filename='log.txt',
                    filemode='w',
                    level=logging.INFO
                    )

LOGGER = logging.getLogger(__name__)


def hello(request):
    LOGGER.info('Nic smiesznego.')
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': ['beautiful', 'cruel', 'wonderful']},
    )


# def movies(request):
#     return render(
#         request,
#         template_name='movies.html',
#         context={'movies': Movie.objects.all(), 'limits': Genre.age_limit_choices}
#     )
# class MovieView(views.View):
#     def get(self, request):
#         return render(
#             request,
#             template_name='movies.html',
#             context={'movies': Movie.objects.all(), 'limits': Genre.age_limit_choices},
#         )

# class MovieView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'movies': Movie.objects.all(), 'limits': Genre.age_limit_choices}

# class MovieView(ListView):
#     template_name = "movies.html"
#     model = Movie
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["limits"] = Genre.age_limit_choices
#         return context


class MovieCreateView(CreateView):
    title = 'Add Movie'
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        title = request._post.get('title')
        if title:
            LOGGER.info(f'Succesfuly added new movie: {title}')

        return result


class MovieUpdateView(UpdateView):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    success_url = reverse_lazy('core:movie_list')


class MovieListView(ListView):
    template_name = "movie_list.html"
    model = Movie

class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie

class IndexView(MovieListView):
    template_name = "index.html"
