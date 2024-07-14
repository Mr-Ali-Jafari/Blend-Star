from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["user"]

        widgets = {
            "first_name": forms.TextInput(attrs={"class":"form-control"}),
            "last_name": forms.TextInput(attrs={"class":"form-control"}),
            "picture": forms.FileInput(attrs={"class":"form-control","type":"file"}),
            "desc": forms.TextInput(attrs={"class":"form-control"}),
            "birthday": forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "gender": forms.Select(attrs={"class":"form-control"}),
            "universe": forms.TextInput(attrs={"class":"form-control"}),

        }