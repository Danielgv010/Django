from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre",required=True,widget=forms.TextInput(
        attrs={'class':'form-control','value':'john'}
    ))
    correo = forms.EmailField(label="Email",required=True,widget=forms.EmailInput(
        attrs={'class':'form-control','value':'jonh@doe.com'}
    ))
    contenido = forms.CharField(label="Contenido",required=True,widget=forms.Textarea(
        attrs={'class':'form-control','placeholder':'Escriba aqui su mensaje'}
    ),min_length=10,max_length=200)