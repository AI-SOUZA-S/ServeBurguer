from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class ExtendedCustomUserCreationForm(UserCreationForm):
    telefone = forms.CharField(max_length=15, label='Telefone')
    nome = forms.CharField(max_length=100, label='Nome', required=True)
    email = forms.EmailField(max_length=255, label='Email', required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('telefone', 'nome', 'email')
