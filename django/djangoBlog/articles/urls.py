from django.urls import path
from . import views

urlpatterns = [
  
    path('',views.articles),
    path('about/',views.articles_list),
    path('details/<int:todo_id>/',views.detail),
    path('create/',views.create,name='create'),
    path('update/',views.update,name='update'),

]
