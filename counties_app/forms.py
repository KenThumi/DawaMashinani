from django import forms
from .models import Counties

class countiesForm(forms.ModelForm):  
    class Meta:  
        model = Counties
        fields = "__all__" 