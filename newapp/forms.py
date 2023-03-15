from dataclasses import field
from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from newapp.models import Posts



class RegisterationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
               "first_name",
               "last_name",
               "username",
               "email",
               "password1",
               "password2",
        ]

        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "password1":forms.TextInput(attrs={"class":"form-control"}),
            "password2":forms.TextInput(attrs={"class":"form-control"})

        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}),label="USERNAME")
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}),label="PASSWORD")
class PostsForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["post","image"]
        widgets={
            "post":forms.Textarea(attrs={"class":"form-control","rows":3}),
            "image":forms.FileInput(attrs={"class":"form-select"}),
        }
        labels={
            "post":"POST",
            "image":"IMAGE",
        }