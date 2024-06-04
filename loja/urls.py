from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.hamburgueria, name="hamburgueria"),
    path('carrinho/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('atualizar_quantidade/', views.atualizar_quantidade, name="atualizar_quantidade"),
    path('criar/', views.criarProduto, name='criar'),
    path('<int:pk>/atualizar/', views.atualizarProduto, name='atualizarProduto'),
    path('<int:pk>/deletar/', views.deletarProduto, name='deletarProduto'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pedido/<int:id_pedido>/', views.pedidoDetalhe, name='pedidoDetalhe'),
    path('pedido/<int:id_pedido>/update/<str:novoStatus>/', views.mudarStatusDoPedido, name='mudarStatusPedido')
]
