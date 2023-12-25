from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
from .forms import CustomUserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import update_session_auth_hash
def home(request):

    return render(request, 'core/home.html')



@login_required

def products(request):

    return render(request, 'core/products.html')


def exit(request):
    logout(request)
    return redirect('home')




def register(request):
    data = {

        'form' : CustomUserCreationForm()

    }


    if request.method == 'POST':

        user_creation_form = CustomUserCreationForm(data = request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username= user_creation_form.cleaned_data['username'], password = user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('home')
    return render(request, 'registration/register.html',data)




#cambiar la contraseña del estudiante

class ProfilePasswordChangeView(PasswordChangeView):
    template_name = 'core/change_password.html'
    success_url = reverse_lazy('products')
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['password_change'] = self.request.session.get('password_change', False)
        return context
    
    def form_valid(self, form):
        messages.success(self.request,'Cambio de contraseña exitoso')
        update_session_auth_hash(self.request,form.user)
        self.request.session['password_change']= True
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,'No se puede cambiar las contraseña')
        
        return super().form_invalid(form)
    