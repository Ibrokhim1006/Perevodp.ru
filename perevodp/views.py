from django.shortcuts import render
from perevodp.models import *

def home(request):
    context = {}
    context['objects_list'] = Catgeoriya.objects.all()
    return render(request, 'perevodp/index.html',context)