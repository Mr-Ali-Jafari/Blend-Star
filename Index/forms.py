from django import forms
from . import models

class CreationPost(forms.ModelForm):
    class Meta:
        model = models.Post
        exclude = ["user"]
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control title"}),
            "desc": forms.Textarea(attrs={"class":"form-control desc"}),
        }


class LikeForm(forms.ModelForm):
    class Meta:
        model = models.Like
        fields = []


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        exclude = ["user","post"]
        widgets = {
            "text": forms.TextInput(attrs={"class":"form-control text-comment"}),
        }