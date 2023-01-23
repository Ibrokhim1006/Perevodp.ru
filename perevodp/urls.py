from django.urls import path
from perevodp.views import *


urlpatterns = [
    path('',home,name='home'),
    path('get_pesni/<int:id>/',get_pesni,name='get_pesni'),
]