from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_servico, name='servicos'),
    path('cadastro/', views.cadastro_servico, name='cadastro_servico'),
    path('detalhes/<int:id>/ajax/', views.detalhes_servico_ajax, name='detalhes_servico_ajax'),
    path('editar/<int:pk>/', views.EditarServico.as_view(), name='editar_servico'),
]