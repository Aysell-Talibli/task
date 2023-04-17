from django import forms

class InstagramForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class Add_intagramForm(forms.Form):
    username = forms.CharField(max_length=100)
