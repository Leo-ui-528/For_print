from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import PrintUser
from django import forms


class PrintUserLoginForm(AuthenticationForm):
    class Meta:
        model = PrintUser
        fields = ('username', 'password')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'


class PrintUserRegisterForm(UserCreationForm):
    class Meta:
        model = PrintUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'position')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PrintUserEditForm(UserChangeForm):
    class Meta:
        model = PrintUser
        fields = ('username', 'first_name', 'password', 'email', 'position')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                if field_name == 'password':
                    field.widget = forms.HiddenInput()