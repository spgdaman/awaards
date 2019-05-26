from .models import Project, Profile
from django import forms

class NewProject(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['id','design_rating','usability_rating','content_rating']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []