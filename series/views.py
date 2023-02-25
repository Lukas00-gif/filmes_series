from django.shortcuts import render

from series.models import Series

# Create your views here.

def pag_series(request):
    series = Series.objects.all()
    return render(request, 'series.html', {'series': series})
