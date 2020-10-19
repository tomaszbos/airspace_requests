from django.shortcuts import render
from django.views.generic import View


class LandingPage(View):
    def get(self, request):
        return render(request, 'index.html')


class AupPreview(View):
    def get(self, request):
        return render(request, 'aup.html')


class AirspaceRequest(View):
    def get(self, request):
        return render(request, 'request.html')
