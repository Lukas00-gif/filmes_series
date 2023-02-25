from django.contrib import admin
from .models import Filmes
from series.models import Series

# Register your models here.

admin.site.register(Filmes)
admin.site.register(Series)

