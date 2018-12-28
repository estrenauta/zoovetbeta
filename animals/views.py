from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Animal
from .forms import AnimalForm, AddVet
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

def create_animal(request):
    if request.user.is_authenticated:
        form = AnimalForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                animal = form.save(commit = False)
                animal.user = request.user
                animal.save()
                form.save_m2m()
            return redirect('index')
        return render(request, 'animal_create.html', {'form': form})
    else:
        return redirect('login')

def edit_animal(request, animal_id):
    if request.user.is_authenticated:
        animal= Animal.objects.get(id= animal_id)
        form = AnimalForm(request.POST or None, instance= animal)
        
        if request.method == 'POST':
            if form.is_valid():
                animal = form.save(commit = False)
                animal.save()
                return redirect('detail_animal', animal.id)
        return render(request, 'animal_edit.html', {'form':form })
    else:
        return redirect('login')

def delete_animal(request, animal_id):
    if request.user.is_authenticated:
        Animal.objects.filter(id= animal_id).delete()
        messages.info(request, 'Your Zoovet was delete!')
        return redirect('index')
    else:
        return redirect('login')
    
def record(request, animal_id):
    user = request.user
    animal = user.animal_set.get(id=animal_id)
    context = {
        'animal': animal
    }
    return render(request, 'record.html', context)

def vetadd(request, animal_id):
    if request.user.is_authenticated:
        animal= Animal.objects.get(id= animal_id)
        form = AddVet(request.POST or None, instance= animal)
        if request.method == 'POST':
            if form.is_valid():
                animal = form.save()
                return redirect('detail_animal', animal.id)
        return render(request, 'uservet_add.html', {'form':form })
    else:
        return redirect('login')

#def services(request, animal_id):
 #   if request.user.is_authenticated:
  #      animal= Animal.objects.get(id= animal_id)
   #     form = Services(request.POST or None, instance= animal)
    #    if request.method == 'POST':
     #       if form.is_valid():
      #          animal = form.save()
       #         return redirect('detail_animal', animal.id)
       # return render(request, 'services.html', {'form':form })
    #else:
     #   return redirect('login')

#def vetedit(request, animal_id):
 #   if request.user.is_authenticated:
  #      animal= Animal.objects.get(id= animal_id)
   #     form = UserForm(request.POST or None, instance= animal)
    #    
     #   if request.method == 'POST':
      #      if form.is_valid():
       #         animal = form.save(commit = False)
        #        animal.save()
         #       return redirect('detail_animal', animal.id)
       # return render(request, 'animal_edit.html', {'form':form })
   # else:
    #    return redirect('login')