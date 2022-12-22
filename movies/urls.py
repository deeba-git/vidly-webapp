from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),

    # we use angular brackets '<>' to define the parameters
    path('<int:movie_id>', views.detail, name='detail')
]
