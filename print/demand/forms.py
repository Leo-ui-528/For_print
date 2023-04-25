from django import forms
from models import Upload
from django.forms import ModelForm


class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ['print_format', 'type_paper', 'folding', 'number_of_instances', 'phone', 'upload_file']
        widgets = {
            "message": Textarea(
                attrs={
                    "placeholder": "Would love to talk about Philip K. Dick"
                }
            )
        }