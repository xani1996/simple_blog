from django import forms
from django.forms import EmailInput, TextInput, Textarea

from .models import Comment
from django.utils.translation import gettext as _


class EmilPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(
        attrs={'placeholder': 'نام شما', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل فرستنده', 'class': 'form-control'}))
    to = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل گیرنده ', 'class': 'form-control'}))
    comments = forms.CharField(required=False,
                               widget=forms.Textarea(attrs={'placeholder': 'نظر شما در  مورد این پست '}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': TextInput(attrs={
                'style': 'width: 300px;',
                'class': "form-control",
                'placeholder': 'نام'
            }),
            'email': EmailInput(attrs={
                'style': 'width: 300px;',
                'class': "form-control text-center",
                'placeholder': 'ایمیل'
            }),
            'body': Textarea(attrs={
                'style': 'width: 300px;',
                'class': "form-control",
                'placeholder': 'متن نظر شما'
            }),
        }


class SearchForm(forms.Form):
    query = forms.CharField()
