from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from demand.models import Upload
from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect


class UploadView(CreateView):
    model = Upload
    fields = ['print_format', 'type_paper', 'folding', 'number_of_instances', 'phone', 'upload_file', 'file']
    success_url = reverse_lazy('fileupload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all()
        return context


@login_required
def will_be(request, **kwargs):
    will = Upload.objects.filter(bool=False)
    return render(request, 'demand/will_be.html', {'will': will})


@login_required
def ended(request, **kwargs):
    end = Upload.objects.filter(bool=True)
    return render(request, 'demand/ended.html', {'end': end})


def update(request):
    if request.method == 'POST':
        doc = Upload.objects.filter(bool=False).update(bool=True)
        messages.add_message(request, messages.INFO, 'Выполнен документ')
        return render(request, 'demand/will_be.html', {'doc': doc})
