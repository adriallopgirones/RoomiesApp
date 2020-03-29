from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]

class JoinGroupForm(forms.Form):
    group_id = forms.CharField(label='id', max_length=100)

class NewGroupForm(forms.Form):
    name = forms.CharField(label='shared list name', max_length=100)