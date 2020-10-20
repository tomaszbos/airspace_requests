from django.shortcuts import render
from django.views.generic import View, FormView, CreateView
from django.urls import reverse_lazy

from .forms import ReservationForm
from .models import AirspaceStructure


class LandingPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class AupPreview(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'aup.html')


class AirspaceRequest(FormView):
    # def get(self, request, *args, **kwargs):
    #     form = ReservationForm()
    #     context = {'form': form}
    #     return render(request, 'request.html', context)
    form_class = ReservationForm
    success_url = reverse_lazy('index')
    template_name = 'request.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
