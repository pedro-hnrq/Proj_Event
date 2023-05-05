from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .forms import CustomPasswordResetForm

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('sair/', views.sair, name="sair"),
    
    path('ativar_conta/<str:token>/', views.ativar_conta, name="ativar_conta"),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html", form_class=CustomPasswordResetForm), name="password_reset"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm_view.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
]