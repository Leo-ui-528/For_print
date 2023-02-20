from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Upload


class UploadView(CreateView):
    model = Upload
    fields = ['print_format', 'type_paper', 'folding', 'number_of_instances', 'phone', 'upload_file']
    success_url = reverse_lazy('fileupload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all()
        return context


def index(request):
    return render(request, 'demand/index.html')


def will_be(request):
    return render(request, 'demand/will_be.html')


def ended(request):
    return render(request, 'demand/ended.html')
