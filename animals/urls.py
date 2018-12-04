from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('animal/detail/<int:animal_id>', views.detail_animal, name="detail_animal")
    #path('animal/create/<int:animal_id>', views.detail_animal, name="detail_animal")
    #path('animal/update/<int:animal_id>', views.detail_animal, name="detail_animal")
    #path('animal/delete/<int:animal_id>', views.detail_animal, name="detail_animal")
]
