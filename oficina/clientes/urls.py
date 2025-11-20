from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('cadastro/', views.cadastro, name='cadastrar_cliente'),
    path('excluir/<int:id>', views.excluir_cliente, name='excluir_cliente'),
    path('editar/<int:pk>/', views.EditarCliente.as_view(), name='editar_cliente'),
]