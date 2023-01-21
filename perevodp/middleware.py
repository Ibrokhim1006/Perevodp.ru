from django.shortcuts import redirect, render
from perevodp.models import *

def get_catgeors_all(get_res):
    def middleware(request):
        request.get_catgor =Catgeoriya.objects.all()
        response = get_res(request)

        return response
    return middleware