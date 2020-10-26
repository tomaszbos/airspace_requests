from django.shortcuts import redirect, render
from django.views.generic import FormView, ListView, View, TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from djgeojson.views import GeoJSONLayerView
from datetime import date
from rest_framework import generics

from .forms import ReservationForm, RegistrationForm
from .models import AirspaceStructure, Aup, Reservation
from .serializers import AupSerializer, ReservationSerializer

User_base = get_user_model()


class StructuresGeoJson(GeoJSONLayerView):
    """
    Creates JSON of Airspace Structures.
    """
    template_name = 'geojson.html'
    queryset = AirspaceStructure.objects.all()
    geometry_field = 'localization'


class AupGeoJson(GeoJSONLayerView):
    """
    Creates JSON of Airspace Structures for valid AUP.
    """
    template_name = 'geojson.html'
    reservations = Reservation.objects.filter(activation_date__exact=date.today())
    queryset_list = []
    for reservation in reservations:
        structure = AirspaceStructure.objects.get(pk=reservation.airspace_structure_id)
        queryset_list.append(structure.pk)
    queryset = AirspaceStructure.objects.filter(pk__in=queryset_list)
    geometry_field = 'localization'


class LandingPage(TemplateView):
    """
    View for landing page.
    """
    template_name = 'index.html'


class AupPreview(TemplateView):
    """
    View for Airspace Use Plan (AUP).
    """
    template_name = 'aup.html'


class AirspaceRequest(LoginRequiredMixin, FormView):
    """
    View for requesting an airspace structure in a form.
    """
    form_class = ReservationForm
    success_url = reverse_lazy('index')
    template_name = 'request.html'

    def form_valid(self, form):
        """
        Validation permission to request an airspace structure.
        """
        structure = form.cleaned_data['airspace_structure']
        structure_type = structure.airspace_type
        if structure_type == 'D' \
                or structure_type == 'R' \
                or structure_type == 'P' \
                or structure_type == 'CTR' \
                or structure_type == 'TMA' \
                or structure_type == 'MCTR' \
                or structure_type == 'MTMA' \
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
    """
    View for user registration.
    """
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
    """
    Login view.
    """
    pass


class UserLogoutView(LogoutView):
    """
    Logout view.
    """
    pass


class AirspaceStructuresView(ListView):
    """
    List of all airspace structures.
    """
    model = AirspaceStructure
    template_name = 'airspace_structures.html'
    context_object_name = 'airspace_structure_list'


class AirspaceManagementView(LoginRequiredMixin, CreateView):
    """
    View with form for adding airspace structure.
    """
    model = AirspaceStructure
    fields = ['name', 'airspace_type', 'lower_limit', 'upper_limit', 'localization']
    success_url = reverse_lazy('airspace_structures_view')
    template_name = 'airspace_form.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)  # TODO: Save to DB!


class AupApiView(generics.ListCreateAPIView):
    """
    REST API for AUP.
    """
    serializer_class = AupSerializer
    queryset = Aup.objects.all()


class ReservationApiView(generics.ListCreateAPIView):
    """
    REST API for reservations.
    """
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
