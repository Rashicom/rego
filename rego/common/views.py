from django.shortcuts import render, redirect
from django.views import View
from .models import Plans, Questions
from django.contrib.auth import authenticate, login
from django.contrib import messages

class HomeView(View):
    def get(self, request):
        products = Plans.objects.all()
        return render(request, "index.html", {"products":products})

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
    


# admin apis
class adminlogin(View):
    def get(self, request):
        return render(request, "admin.html")
    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Log in the user
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("admindashboard")
        else:
            messages.error(request, "Invalid username or password.")
        return render(request, 'admin.html')
    
    
class admindashboard(View):
    def get(self, request):
        return render(request, "admindash.html")
    
class adminplans(View):
    def get(self, request):
        plans = Plans.objects.all()
        return render(request, "plan.html", {"plans": plans})
    

class QuestionsView(View):
    def get(self, request):
        questions = Questions.objects.all()
        return render(request, "questions.html", {"questions":questions})
    