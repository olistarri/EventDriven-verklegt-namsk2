from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.forms import widgets, ModelForm
from user.models import User
from django_countries import countries

COUNTRY_CHOICES = countries


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
        self.fields['username'].help_text = 'Required. 25 characters or fewer. Letters, digits and @/./+/-/_ only.<br>'

class PaymentInfoForm(forms.Form):
    sendhome = forms.BooleanField(required=False, label="I want the ticket sent home", widget=forms.CheckboxInput(attrs={'id': 'sendhome'}))
    cardholder_name = forms.CharField(label='Name on card', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cardnumber = forms.CharField(label='Card number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    exp_date = forms.CharField(label='Expiration date', max_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'exp'}))
    cvc = forms.IntegerField(label='CVC (on back of card)', max_value=999,
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))
    name = forms.CharField(required=False, label='Full name', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, label='Address', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(required=False, label='City', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.ChoiceField(required=False, choices=COUNTRY_CHOICES, widget=widgets.Select(attrs={'class': 'form-control'}))
    zip = forms.CharField(required=False, label='Postal code', widget=forms.TextInput(attrs={'class': 'form-control'}))


class PaymentForm(forms.Form):
    cardholder_name = forms.CharField(label='Name on card', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cardnumber = forms.CharField(label='Card number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    exp_date = forms.CharField(label='Expiration date', max_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'exp'}))
    cvc = forms.IntegerField(label='CVC (on back of card)', max_value=999,
                             widget=forms.NumberInput(attrs={'class': 'form-control'}))


class UserEditForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'password', 'last_name', 'is_superuser', 'groups', 'last_login', 'user_permissions',
                   'is_staff', 'is_active', 'date_joined']
        widgets = {
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': widgets.ClearableFileInput(attrs={'class': 'form-control'}),

        }

class ChangePasswordForm(PasswordChangeForm):
    class Meta(PasswordChangeForm):
        model = User
        widgets ={
            'new_password1': widgets.TextInput(attrs={'class': 'form-control'}),
            'new_password2': widgets.TextInput(attrs={'class': 'form-control'}),
            'old_password': widgets.TextInput(attrs={'class': 'form-control'}),
        }
