from django import forms
from .models import *

class MedicineForm(forms.ModelForm):
    
    class Meta:
        model = Medicine
        fields = ('category','genericName')
    
