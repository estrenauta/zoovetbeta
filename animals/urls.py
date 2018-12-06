from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('animal/detail/<int:animal_id>', views.detail_animal, name="detail_animal"),
    path('animal/create/', views.create_animal, name="animal_create"),
    path('animal/edit/<int:animal_id>', views.edit_animal, name="animal_edit"),
    path('animal/delete/<int:animal_id>', views.delete_animal, name="animal_delete"),
]
