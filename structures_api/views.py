from django.shortcuts import redirect, render
from django.views.generic import DetailView, FormView, ListView, View
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ReservationForm, RegistrationForm
from .models import AirspaceStructure

User_base = get_user_model()


class LandingPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class AupPreview(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'aup.html')


class AirspaceRequest(LoginRequiredMixin, FormView):
    form_class = ReservationForm
    success_url = reverse_lazy('index')
    template_name = 'request.html'

    def form_valid(self, form):
        structure = form.cleaned_data['airspace_structure']
        structure_type = structure.airspace_type
        if structure_type == 'D'\
                or structure_type == 'R'\
                or structure_type == 'P'\
                or structure_type == 'CTR'\
                or structure_type == 'TMA'\
                or structure_type == 'MCTR'\
                or structure_type == 'MTMA'\
                or structure_type == 'ADIZ':
            return render(self.request, 'access_denied.html')
        elif structure_type == 'TSA' and not self.request.user.has_perm('structures_api.request_tsa'):
            return render(self.request, 'access_denied.html')
        elif structure_type == 'TRA' and not self.request.user.has_perm('structures_api.request_tra'):
            return render(self.request, 'access_denied.html')
        elif structure_type == 'EA' and not self.request.user.has_perm('structures_api.request_ea'):
            return render(self.request, 'access_denied.html')
        elif structure_type == 'ATZ' and not self.request.user.has_perm('structures_api.request_atz'):
            return render(self.request, 'access_denied.html')
        elif structure_type == 'MRT' and not self.request.user.has_perm('structures_api.request_mrt'):
            return render(self.request, 'access_denied.html')
        form.save()
        return super().form_valid(form)


class RegisterUser(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            return redirect('login')
        else:
            return render(request, 'registration/register.html', {'form': form})


class LoginUserView(LoginView):
    pass


class UserDetailView(DetailView):
    model = User_base

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context  # TODO: Fix the view!


class UserLogoutView(LogoutView):
    pass


class AirspaceStructuresView(ListView):
    model = AirspaceStructure
    template_name = 'airspace_structures.html'
    context_object_name = 'airspace_structure_list'
