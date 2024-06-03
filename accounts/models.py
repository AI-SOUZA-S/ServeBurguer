from django.db import models
from django import forms
from .admin import CustomUserCreationForm 
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=15)
    nome = models.CharField(max_length=150)  
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = 'Usuário Personalizado'
        verbose_name_plural = 'Usuários Personalizados'

# Definindo o related_name exclusivo para o relacionamento de grupos
CustomUser.groups.field.remote_field.related_name = 'customuser_groups'

# Definindo o related_name exclusivo para o relacionamento de permissões
CustomUser.user_permissions.field.remote_field.related_name = 'customuser_permissions'

