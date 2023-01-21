from django.urls import path
from perevodp.views import *


urlpatterns = [
    path('',home,name='home'),
    path('get_catgor/<int:id>/',get_categor,name='get_categor'),
    path('author_pesni/<int:id>/',author_pesni,name='author_pesni'),
    path('get_pesni/<int:id>/',get_pesni,name='get_pesni'),
    path('kontakt/',kontakt,name='kontakt')
]