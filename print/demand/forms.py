from django import forms
from models import Upload
from django.forms import ModelForm


class DocumentForm(forms.ModelForm):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes')


