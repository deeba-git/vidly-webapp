from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    # with this we get the all movies in our database
    movies = Movie.objects.all()

    # rendering html template
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    # pk stands for primary key, we can either use 'id' as well
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
