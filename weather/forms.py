from .models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={
            'name': 'city',
            'id': 'city',
            'class': 'form-control',
            'placeholder': "Введите город"
        })}
