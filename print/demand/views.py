from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from demand.models import Upload


class UploadView(CreateView):
    model = Upload
    fields = ['print_format', 'type_paper', 'folding', 'number_of_instances', 'phone', 'upload_file']
    success_url = reverse_lazy('fileupload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all()
        return context


def will_be(request):
    will = Upload.objects.order_by('upload_date')
    return render(request, 'demand/will_be.html', {'will': will})


def ended(request):
    end = Upload.objects.filter(bool=True)
    return render(request, 'demand/ended.html', {'end': end})










