from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Your login info is not correct. Please check your email and password and try again.')
        return cleaned_data

# НАСТРОИТЬ ОТОБРОЖЕНИ ОШИБКИ ШО НЕПРАВЕЛЬНО ВВЕДЕНІ ДАННІЕ


class UserRegistrationForm(UserCreationForm):

    email = forms.CharField()
    name = forms.CharField(required=False)
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ["email", "name", "password1", "password2"]


class ProfileForm(UserChangeForm):

    email = forms.CharField()
    name = forms.CharField(required=False)
    image = forms.ImageField(required=False)


    class Meta:
        model = User
        fields = ["email", "name", "image"]
