"""airspace_request URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from structures_api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('structures_geo_json', views.StructuresGeoJson.as_view(), name='structures_geo_json'),
    path('aup_geo_json', views.AupGeoJson.as_view(), name='aup_geo_json'),
    path('aup_api', views.AupApiView.as_view(), name='aup_api'),
    path('reservation_api', views.ReservationApiView.as_view(), name='reservation_api'),
    path('', views.LandingPage.as_view(), name='index'),
    path('aup/', views.AupPreview.as_view(), name='aup'),
    path('request/', views.AirspaceRequest.as_view(), name='request'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('accounts/profile/<int:pk>/', views.UserDetailView.as_view(), name='user'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('airspace_structures/', views.AirspaceStructuresView.as_view(), name='airspace_structures_view'),
    path('airspace_management/', views.AirspaceManagementView.as_view(), name='airspace_management'),
]
