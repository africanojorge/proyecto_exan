from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import LoginForm 

# Create your views here.
app_name = 'usuarios' 
def login_view(request):
    form = LoginForm(data=request.POST or None)
    
    if form.is_valid():
        usuario = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if usuario:
            login(request, usuario)
            return redirect('index') 
    
    return render(request, 'usuarios/login.html', {'form': form})
