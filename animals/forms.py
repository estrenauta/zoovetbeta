from django import forms
from .models import Animal

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
            'castrating'
        )

        