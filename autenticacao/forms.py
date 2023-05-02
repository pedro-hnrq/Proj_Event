from django import forms
from django.contrib.auth.forms import PasswordResetConfirmForm
from django.contrib import messages
from django.contrib.messages import constants
import re

class CustomPasswordResetConfirmForm(PasswordResetConfirmForm):
    password1 = forms.CharField(label='Nova senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a nova senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem!")
        if len(password1) < 4:
            raise forms.ValidationError("Sua senha deve conter 4 ou mais caracteres!")
        return password2
