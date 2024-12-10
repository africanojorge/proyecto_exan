from django import forms
from .models import Usuario 
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    pass

class EmpleadoRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmar Contraseña'}))
       
    class meta:
        model = Usuario 
        fields = ['username', 'first_name', 'last_name', 'email', 'rol']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre de Usuario'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Correo Electronico'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden')
            
        return cleaned_data
           
        
        

        
        
    