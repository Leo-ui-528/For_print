from django import forms
from models import Upload
from django.forms import ModelForm


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Upload
        upload_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))




