from django.http import request
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Center
from .data_to_db.csv_to_db import get_screening

def list(request):
    centers = Center.objects.all()

    if len(centers):
        q = request.GET.get('q', '')
        if q: 
            centers = centers.filter(address__icontains=q)

        # Pagination
        if len(centers) <= 60:
            context = {
                'screenings': centers
            }
        else:
            paginator = Paginator(centers, 60) 
            page = request.GET.get('page')
            try:
                screenings = paginator.page(page)
            except PageNotAnInteger:
                screenings = paginator.page(1)
            except EmptyPage:
                screenings = paginator.page(paginator.num_pages)
            
            context = {
                'state': False,
                'screenings': screenings
            }

        return render(request, 'list.html', context)
    else:
        try:
            get_screening()
            
            return redirect('list')
        except:

            context = {
                'state': True,
            }

            return render(request, 'list.html', context)
