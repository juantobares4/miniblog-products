from django.contrib.auth import (
        authenticate, 
        login, 
        logout
    )

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import (
    View,

)

from users.forms import UserRegisterForm

# Create your views here.

class LoginView(View):
    def get(self, request): # Renderiza el formulario.
        return render(
            request, 
            'home/login.html'
        
        )
    
    def post(self, request): # Información que envía el usuario.
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(
                request,
                username = username,
                password = password

            )

            if user:
                login(request, user) # Hacemos uso de la función que importamos más arriba

                return redirect('index')
        
        return redirect('login')
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        
        return redirect('login')
    
class RegisterView(View):
    form_class = UserRegisterForm
    template = 'home/register.html'

    def get(self, request):
        form = self.form_class()
        
        return render(
            request,
            self.template,
            dict(
                form = form

            )

        )
    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')

        else:
            return render(
                request,
                self.template,
                dict(
                    form = form

                )

            )      

@login_required(login_url = 'login') # Se necesita estar logeado, en caso no estarlo, nos envía al login.   
def index_view(request):
    return render(
        request,
        'home/index.html'

    )

