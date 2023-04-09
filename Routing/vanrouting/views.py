from django.shortcuts import render, HttpResponse
from .models import Vaninfo, Institutes_details

# Create your views here.
def index(request):
    Institutes = Institutes_details.objects.all()
    return render(request, 'vanrouting/Institutes.html',{
        'institues':Institutes
    })


def Institute_vans(request, institute_slug):
    vans=Vaninfo.objects.all()
    selected_institute = Institutes_details.objects.get(institute_slug=institute_slug)
    return render(request, 'vanrouting/InstituteVans.html',{
        'vans':vans,
        'institute':selected_institute
    })

def TracedVan(request, van_slug):
    selected_van = Vaninfo.objects.get(van_slug = van_slug)
    return render(request, 'vanrouting/TracedVan.html',{
        'van': selected_van
    })
         