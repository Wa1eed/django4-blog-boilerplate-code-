from django import forms
from .models import Post

class Postform(forms.ModelForm):
    title =forms.CharField(
        required=True,
        widget = forms.widgets.TextInput(
            attrs={
                "placeholder": "please input title here",
                "class": "form-control",

            }
        ), label="title"
    )
    
    body =forms.CharField(
        required=True,
        widget = forms.widgets.Textarea(
            attrs={
                "placeholder": "please input post here",
                "class": "form-control",
            }
        ), label="body"
    )
    image = forms.FileField(
        required=True,
        widget = forms.widgets.ClearableFileInput(
            attrs={
                "class": "form-control",
            }
        ),label="Upload"
    )
    
    class Meta:
        model = Post
        exclude = ("author","date")