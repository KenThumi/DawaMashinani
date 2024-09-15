from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from field_officers_app.models import field_officers

class UserForm(UserCreationForm):
    role = forms.ChoiceField(choices=[('field officer', 'field officer')])
    phone_number = forms.CharField(max_length=10)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'role', 'username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not field_officers.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is not registered in the system. Please use the correct username.")
        return username

class UserLoginForm(forms.Form):
    # role = forms.ChoiceField(choices=[(name, name) for name in CustomUser.objects.values_list('role', flat=True).distinct()])

    db_roles = [(name, name) for name in CustomUser.objects.values_list('role', flat=True).distinct()]

    sl_role = [  
                ('','--select--')
             ]
    
    roles =  sl_role+db_roles

    role =  forms.CharField( widget=forms.Select(choices=roles))
    
    username = forms.CharField(max_length=100)

    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['role'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Role',
        })

        self.fields['username'].widget.attrs.update({
            'class':'form-control',
            'placeholder':'username',
        })

        self.fields['password'].widget.attrs.update({
            'class':'form-control',
        })