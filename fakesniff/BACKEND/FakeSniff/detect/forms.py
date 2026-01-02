from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    agree = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Passwords do not match.")
        return confirm_password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)

