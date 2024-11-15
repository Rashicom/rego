from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, "index.html")

class BuisinessView(View):
    def get(self, request):
        return render(request, "buisness.html")
    
class eventsView(View):
    def get(self, request):
        return render(request, "events.html")

class franchiseView(View):
    def get(self, request):
        return render(request, "franchise.html")
    
class privacypolicyView(View):
    def get(self, request):
        return render(request, "privacypolicy.html")

class termsandconditionsView(View):
    def get(self, request):
        return render(request, "termsandconditions.html")

