from django.shortcuts import render
from perevodp.models import *

def home(request):
    context = {}
    context['objects_list'] = Pesni.objects.all()
    return render(request, 'perevodp/index.html',context)

def get_pesni(request,id):
    context = {}
    context['objects_list'] = Pesni.objects.all()
    context['object'] = Pesni.objects.get(id=id)
    return render(request,'perevodp/get_pesni.html',context)
