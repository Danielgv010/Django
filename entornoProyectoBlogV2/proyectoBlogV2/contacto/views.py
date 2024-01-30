from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactoForm
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    contacto_form = ContactoForm()
    if(request.method=="POST"):
        nom = request.POST.get('nombre')
        cor = request.POST.get('correo')
        cont = request.POST.get('contenido')

        # enviar un correo con el mesaje recibido a atencionCliente
        # Crear el objeto para enviar el correo
        emailEnviar = EmailMessage(
            # Asunto
            "Nuevo mensaje de contacto",
            # Cuerpo
            f"de {nom}-{cor}\n\n Escribió: \n {cont}",
            # Email Origen
            "nocontestar@miempresa.com",
            # Email Destino (lista)
            ["atencionCliente@miempresa.com"],
            # Responder a
            reply_to=[cor],
            bcc=["atencionCliente@miempresa.com","atencionCliente2@miempresa.com"]
        )

        try:
            emailEnviar.send()
        except Exception as e:
            # Manejo de errores
            print(f"Error al enviar el correo: {e}")

        contacto_form = ContactoForm(data=request.POST)
        return redirect(reverse('contacto')+'?ok')

    return render(request,"contacto/contacto.html",{'formulario':contacto_form})