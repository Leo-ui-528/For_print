from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from demand.models import Upload
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django import forms
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)


FOLDING = [
    ('A3', 'А3'),
    ('A4', 'А4'),
    ('Нет', 'Нет'),
]
FORMAT = [
    ('A4', 'A4'),
    ('A3', 'A3'),
    ('A2', 'A2'),
    ('A1', 'A1'),
    ('A0', 'A0'),
]
TYPE = [
    ('Обычная', 'Обычная'),
    ('Плотная', 'Плотная')
]


class UploadView(CreateView):
    model = Upload
    fields = ['print_format', 'type_paper', 'folding', 'number_of_instances', 'phone', 'upload_file']
    success_url = reverse_lazy('fileupload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all().order_by('-upload_date')
        return context

    def get_form(self, form_class=None, **kwargs):
        form = super(UploadView, self).get_form(form_class)
        form.fields['folding'].widget = forms.RadioSelect(attrs={'name': 'rating'}, choices=FOLDING)
        form.fields['print_format'].widget = forms.RadioSelect(attrs={'name': 'rating'}, choices=FORMAT)
        form.fields['type_paper'].widget = forms.RadioSelect(attrs={'name': 'rating'}, choices=TYPE)
        form.fields['upload_file'].widget = forms.ClearableFileInput(attrs={'multiple': True})
        form.fields['number_of_instances'].widget=forms.NumberInput(attrs={"class": "myfield"})
        form.fields['phone'].widget = forms.NumberInput(attrs={"class": "phone"})
        return form


def will_be(request, **kwargs):
    user = get_current_authenticated_user()
    will = Upload.objects.filter(bool=False, cuser=user)
    if user.username == 'admin':
        will = Upload.objects.filter(bool=False)
    return render(request, 'demand/will_be.html', {'will': will})


def ended(request, **kwargs):
    end = Upload.objects.filter(bool=True)
    return render(request, 'demand/ended.html', {'end': end})


def update(request):
    if request.method == 'POST':
        doc = Upload.objects.filter(bool=False).update(bool=True)
        messages.add_message(request, messages.INFO, 'Выполнен документ №')
        return render(request, 'demand/will_be.html', {'doc': doc})
