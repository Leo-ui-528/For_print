from django.contrib.auth.forms import AuthenticationForm

from authapp.models import PrintUser


class PrintUserLoginForm(AuthenticationForm):

    class Meta:
        model = PrintUser
        fields = ('username', 'password')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
