from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save animal'))
        
       # model = Uservet
    
       # fields = (
        #    'name',
        #   'adoption_day',
        #    'species',
        #    'breed',
        #    'color',
        #    'sex',
        #    'castrating'
        #)
