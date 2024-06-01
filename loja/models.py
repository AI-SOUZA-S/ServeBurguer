from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Produto(models.Model):
    opcoes = [
        ('hamburguer', 'Hamburguer'),
        ('bebida', 'Bebida'),
        ('molho', 'Molho'),
        ('porcao', 'Porção'),
    ]
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    imagem = models.ImageField(upload_to='static/images/', blank=True)
    quantidade = models.IntegerField(default=0, validators=[MinValueValidator(1)])
    tipo = models.CharField(max_length=20, choices=opcoes)
    
class Cliente(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=50)
    
class Pedido(models.Model):
    cliente =  models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    data_Pedido = models.DateTimeField(auto_now_add=True)
    completo = models.BooleanField(max_length=100, null=True)
    status = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),    
        ]
    
class ItensPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    dataAdicionado = models.DateTimeField(auto_now_add=True)