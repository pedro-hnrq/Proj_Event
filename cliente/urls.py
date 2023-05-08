from django.urls import path
from . import views

urlpatterns = [
    path('meus_certificados/', views.meus_certificados, name="meus_certificados"),
    path('gerenciar/', views.gerenciar, name='gerenciar'),
    path('excluir_evento/<int:id>', views.excluir_evento, name="excluir_evento"),
    path('editar_evento/<int:id>', views.editar_evento, name="editar_evento"),
]