from django.shortcuts import render
from perevodp.models import *

def home(request):
    context = {}
    context['objects_list'] = Artist.objects.all().order_by('-id')[:4]
    return render(request, 'perevodp/index.html',context)


def get_categor(request,id):
    context = {}
    context['a_z_list'] = Catgeoriya.objects.get(id=id) 
    context['objects_list'] = Artist.objects.filter(catgeor_id=id)
    return render(request,'perevodp/categor.html',context)

def author_pesni(request,id):
    context = {}
    context['artist'] = Artist.objects.get(id=id) 
    context['objects_list'] = Pesni.objects.filter(id_artist=id)
    return render(request,'perevodp/author.html',context)

def get_pesni(request,id):
    context = {}
    context['object'] = Pesni.objects.get(id=id)
    return render(request,'perevodp/get_pesni.html',context)

def kontakt(request):
    return render(request,'perevodp/kontakt.html')