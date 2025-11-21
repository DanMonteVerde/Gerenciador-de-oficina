from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='veiculos'),
    path('cadastro/', views.cadastro_veiculo, name='cadastro_veiculo'),
    path('excluir/<int:id>', views.excluir_veiculo, name='excluir_veiculo'),
    path('editar/<int:pk>/', views.VeiculoUpdateView.as_view(), name='editar_veiculo'),
]