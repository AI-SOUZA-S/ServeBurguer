from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Pedido, ItensPedido
from .forms import FormularioProduto
from django.http import HttpResponse, HttpResponseRedirect
from .whatsapp_service import send_whatsapp_message
from decimal import Decimal
from django.http import JsonResponse

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


def mudarStatusDoPedido(request, id_pedido, novoStatus):
    pedido = get_object_or_404(Pedido, id=id_pedido)
    pedido.status = novoStatus
    pedido.save()
    
    messagem = f'Olá {pedido.cliente.nome}, seu pedido está agora {novoStatus.replace("_", ' ').lower()}.'
    send_whatsapp_message(pedido.cliente.telefone, messagem)
    
    return redirect('pedidoDetalhe', id_pedido=id_pedido)

def pedidoDetalhe(request, id_pedido):
    pedido = get_object_or_404(Pedido, id=id_pedido)
    itens_pedido = get_object_or_404(ItensPedido, pedido=pedido)
    return render(request, 'pedidoDetalhe.html', {'pedido': pedido, 'itens_pedido': itens_pedido})

def cart(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        
        carrinho = request.session.get('carrinho', [])
        carrinho.append(produto_id)
        request.session['carrinho'] = carrinho
        
        return HttpResponseRedirect('/carrinho/')  # Redireciona para a página do carrinho
    
    else:
        carrinho = request.session.get('carrinho', [])
        produtos_no_carrinho = Produto.objects.filter(pk__in=carrinho)
        itens = len(produtos_no_carrinho)
        
        for produto in produtos_no_carrinho:
            produto.preco *= Decimal(produto.quantidade)
        total = sum(produto.preco for produto in produtos_no_carrinho)
        
        return render(request, 'hamburgueria/cart.html', {'produtos': produtos_no_carrinho, 'total':total, 'itens':itens})
    
    
def atualizar_quantidade(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        action = request.POST.get('action')

        produto = Produto.objects.get(pk=produto_id)

        if action == 'aumentar':
            produto.quantidade += 1
        elif action == 'diminuir' and produto.quantidade > 1:
            produto.quantidade -= 1
        
        produto.save()

        # Redireciona de volta para a página de carrinho
        return redirect('cart')

    else:
        # Se a solicitação não for POST, retorna uma resposta JSON com erro
        return JsonResponse({'error': 'Método de solicitação inválido'})

def checkout(request):
    carrinho = request.session.get('carrinho', [])
    produtos_no_carrinho = Produto.objects.filter(pk__in=carrinho)
    itens = len(produtos_no_carrinho)
        
    for produto in produtos_no_carrinho:
        produto.preco *= Decimal(produto.quantidade)
    total = sum(produto.preco for produto in produtos_no_carrinho)
    
    return render(request, "hamburgueria/checkout.html", {'produtos': produtos_no_carrinho, 'total':total, 'itens':itens})