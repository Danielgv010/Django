from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django import forms

# Create your views here.


class Registro(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login') +"?registroOk"
    
    def get_form(self, form_class=None):
        form = super(Registro,self).get_form()

        #modificar campos
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de usuario'})
        form.fields['password1'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Repite la Contraseña'})

        for fieldname in ['username','password1','password2']:
            form.fields[fieldname].label = ""
        
        return form