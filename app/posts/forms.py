from django import forms
from django.db import models


class PostCreateForm(forms.Form):
    """
    이 Form에 들어갈 입력 요소
        Image(File)
        Text
    """
    Image = forms.ImageField()
    Text = forms.CharField()

