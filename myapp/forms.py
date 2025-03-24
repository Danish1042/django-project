from django import forms
from .models import Chaiverity

class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(
        queryset=Chaiverity.objects.all(), 
        label="Select Chai Variety",
        widget=forms.Select(attrs={
            'class': 'w-full p-2 border border-gray-300 rounded-md bg-white text-gray-700 focus:outline-none focus:ring focus:ring-blue-300'
        })
    )
