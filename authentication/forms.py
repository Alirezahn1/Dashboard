from django import forms
from django.contrib.auth.models import User


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','email',)
        widgets = {

            'email': forms.EmailInput(attrs={'class': 'email form-control my-2', 'placeholder': 'Enter your Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter your last name'}),
        }