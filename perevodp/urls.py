from django.urls import path
from perevodp.views import *


urlpatterns = [
    path('',home,name='home'),
]