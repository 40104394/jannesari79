from django.urls import path
from . import views

urlpatterns = [
    path('i', views.In, name = 'in'),
    path('o', views.Out, name = 'out'),
   
]