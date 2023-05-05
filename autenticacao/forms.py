from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import gettext as _

class CustomPasswordResetForm(PasswordResetForm):
    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        if len(password1) < 4:
            raise forms.ValidationError(_('Sua senha deve conter 4 ou mais caracteres.'), code='password_too_short')

        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError(_('Sua senha não contém números.'), code='password_no_number')

        if not any(char.isupper() for char in password1):
            raise forms.ValidationError(_('Sua senha não contém letras maiúsculas.'), code='password_no_uppercase')

        if not any(char.islower() for char in password1):
            raise forms.ValidationError(_('Sua senha não contém letras minúsculas.'), code='password_no_lowercase')

        return password1
