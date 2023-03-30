from django import forms
from core.models import User

from django.contrib.auth.forms import UserChangeForm


class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields='__all__'

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model= User
        fields='__all__'
