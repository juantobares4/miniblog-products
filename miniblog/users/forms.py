from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text='Email requerido',
        widget=forms.EmailInput(attrs={'class': 'form-control m-3', 'required': 'required'})
    
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control m-3'})
    
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control m-3'})
    
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name'

        ]

        widgets = {
            'username': forms.TextInput(attrs = {'class': 'form-control m-3', 'required': 'required'}),
            
            'email': forms.EmailInput(attrs = {'class': 'form-control m-3', 'required': 'required'}),

            'first_name': forms.TextInput(attrs = {'class': 'form-control m-3', 'required': 'required'}),
            
            'last_name': forms.TextInput(attrs = {'class': 'form-control m-3', 'required': 'required'})

        }

        def clean_email(self):
            email = self.cleaned_data.get('email')
            email_exists = User.objects.filter(email = email).exists()
            
            if email_exists:
                raise ValidationError('¡El email ingresado ya existe!')
            
            return email
        
        def save(self, commit = True):
            user = super().save(commit = False)
            user.email = self.cleaned_data.get('email')
            user.is_staff = False
            user.is_superuser = False

            if commit:
                user.save()
            
            return user

