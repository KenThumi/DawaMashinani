from django import forms
from .models import field_officers
from counties_app.models import Counties

class field_officersForm(forms.ModelForm): 
    county = forms.ChoiceField(choices=[(name, name) for name in Counties.objects.values_list('county_name', flat=True).distinct()]) 
    class Meta:  
        model = field_officers
        fields = ['fname', 'lname', 'email', 'phone', 'county', 'username']