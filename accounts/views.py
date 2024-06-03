from django.shortcuts import render, redirect
from .admin import CustomUserCreationForm
from django.contrib import messages
from .formulario import ExtendedCustomUserCreationForm 


# Create your views here.
def register(request):
    form = ExtendedCustomUserCreationForm()
    if request.method == "POST":
        form = ExtendedCustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            telefone = form.cleaned_data.get('telefone')
            user.telefone = telefone
            user.save()
            messages.success(request, 'Registrado. Agora faça o login para começar!')
            return redirect('hamburgueria')

        else:
            print('Detalhes de registro inválidos')
            
    return render(request, "registration/register.html",{"form": form})



