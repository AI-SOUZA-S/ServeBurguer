from django.shortcuts import render, redirect
from .models import Produto
from .forms import FormularioProduto
from django.http import HttpResponse, HttpResponseRedirect


def hamburgueria(request):
    hamburgueres = []
    bebidas = []
    molhos = []
    porcoes = []
    produtos = Produto.objects.all()
    print(produtos)
    for produto in produtos:
        if produto.tipo == 'hamburguer':
            hamburgueres.append(produto)
            print(hamburgueres)
        elif produto.tipo == 'bebida':
            bebidas.append(produto)
            print(bebidas)
        elif produto.tipo == 'molho':
            molhos.append(produto)
            print(molhos)
        elif produto.tipo == 'porcao':
            porcoes.append(produto)
            print(porcoes)
    
    
    return render(request, 'hamburgueria/hamburgueria.html', {
        'hamburgueres': hamburgueres,
        'bebidas': bebidas,
        'molhos': molhos,
        'porcoes': porcoes
    })
            

def cart(request):
    context = {}
    return render(request, "hamburgueria/cart.html", context)

def checkout(request):
    context = {}
    return render(request, "hamburgueria/checkout.html",context)


def criarProduto(request):
    
    if request.method == 'POST':
        
        form = FormularioProduto(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect ('/hamburgueria/')
        
            
            
    else:
        form = FormularioProduto()      
        
    return render(request, 'produto/criarProduto.html', {'form':form})

        
        
        
def atualizarProduto(request, pk):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        formulario = FormularioProduto(request.POST, instance=produto)
        if formulario.is_valid():
            formulario.save()
            return redirect('listaProdutos')
    else:
        formulario = FormularioProduto(instance=produto)
        return render(request, 'atualizarProduto.html', {'formulario': formulario})
        

def deletarProduto(request, pk):
    Produto.objects.get(pk=pk).delete()
    return redirect('listaProdutos')