from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user = request.user
        user_animals = user.animal_set.all()  #aqui tmb irian los veterinarios 
        print(user_animals)
        context = {
            'animals': user_animals
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html')

def detail_animal(request, animal_id):
    user = request.user
    animal = user.animal_set.get(id=animal_id)
    context = {
        'animal': animal
    }
    return render(request, 'detail.html', context)

