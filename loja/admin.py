from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(ItensPedido)
