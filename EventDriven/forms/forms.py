from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import widgets
from user.models import User


class CustomAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control'}
        )

class RegisterUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_picture')
        widgets = {

            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={ 'class': 'form-control'}),
            'date_of_birth': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': widgets.TextInput(attrs={ 'class': 'form-control'}),
            'profile_picture': widgets.ClearableFileInput(attrs={ 'class': 'form-control'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['username'].help_text = 'Required. 25 characters or fewer. Letters, digits and @/./+/-/_ only. <br>'
