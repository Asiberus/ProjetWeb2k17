from django import forms

class AdminLoginForm(forms.Form):
    user = forms.CharField(max_length=50)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)