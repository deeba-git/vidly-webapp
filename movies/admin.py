from django.contrib import admin
from .models import Genre, Movie

# Register your models here.


class GenreAdmindk(admin.ModelAdmin):
    list_display = ("id", "name")


class MovieAdmin(admin.ModelAdmin):
    exclude = ("date_created",)
    list_display = ("title", "release_year", "number_in_stock")


admin.site.register(Genre, GenreAdmindk)
admin.site.register(Movie, MovieAdmin)
