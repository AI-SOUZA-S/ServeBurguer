from django import forms
from .models import Produto

class FormularioProduto(forms.ModelForm):
    
    escolhas = [
        ('hamburguer', 'Hamburguer'),
        ('bebida', 'Bebida'),
        ('molho', 'Molho'),
        ('porcao', 'Porção'),
    ]

    tipo = forms.ChoiceField(choices=escolhas, widget=forms.RadioSelect)
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'imagem', 'quantidade', 'tipo']