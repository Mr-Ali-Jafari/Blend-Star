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