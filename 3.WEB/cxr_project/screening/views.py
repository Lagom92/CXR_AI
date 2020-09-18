from django.http import request
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Center

def list(request):
    centers = Center.objects.all()

    # Pagination
    paginator = Paginator(centers, 60) 
    page = request.GET.get('page')
    try:
        screenings = paginator.page(page)
    except PageNotAnInteger:
        screenings = paginator.page(1)
    except EmptyPage:
        screenings = paginator.page(paginator.num_pages)
    
    context = {
        'screenings': screenings
    }

    return render(request, 'list.html', context)