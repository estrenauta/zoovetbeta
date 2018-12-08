from django import forms
from .models import Animal, UserProfile

class AnimalForm(forms.ModelForm):
    
    class Meta:
        model = Animal
    
        fields = (
            'name',
            'adoption_day',
            'species',
            'breed',
            'color',
            'sex',
            'castrating',
            'vets'
        )

class UserProfileform(forms.ModelForm):
    class Meta:
        model = UserProfile

        fields = (
            'street',
            'colony',
            'state',
            'country',
            'phone'
        )

class AddVet(forms.ModelForm):
    class Meta:
        model = Animal

        fields = (
            'vets',
        )
