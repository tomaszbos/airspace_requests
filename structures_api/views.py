from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, FormView, ListView, View
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView

from .forms import ReservationForm, RegistrationForm
from .models import AirspaceStructure, Aup, Reservation

User_base = get_user_model()


class LandingPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class AupPreview(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'aup.html')


class AirspaceRequest(FormView):
    form_class = ReservationForm
    success_url = reverse_lazy('index')
    template_name = 'request.html'

    def form_valid(self, form):
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
        return context # TODO: Fix the view!


class UserLogoutView(LogoutView):
    pass


class AirspaceStructuresView(ListView):
    model = AirspaceStructure
    paginate_by = 25
    template_name = 'airspace_structures.html'
    context_object_name = 'airspace_structure_list'
