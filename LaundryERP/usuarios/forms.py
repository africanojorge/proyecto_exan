from django import forms
from .models import Usuario 
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    pass
        
        
        
    '''class Empleadoform(forms.ModelForm):
    ROLES = [
        ('admin', 'Administrador'),
        ('empleado', 'Empleado'),
    ]

    nombre=forms.CharField(max_length=100)
    rol = forms.ChoiceField(choices=ROLES, initial='empleado')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password'] '''
        