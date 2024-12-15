from django.shortcuts import render, redirect
from django.views import View
from .models import Plans, Questions, Contactinfo, PlanFeatures
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ContactForm, QuestionForm, PlanForm
import json
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(View):
    def get(self, request):
        products = Plans.objects.all()
        questions = Questions.objects.all()
        contact = Contactinfo.objects.all().last()
        return render(request, "index.html", {"products":products, "questions":questions, "contact":contact})

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


class AdminLogout(View):
    def get(self, request):
        logout(request)
        return redirect("adminlogin")


class admindashboard(LoginRequiredMixin,View):
    login_url = 'adminlogin'
    def get(self, request):
        contact = Contactinfo.objects.all().last()
        return render(request, "admindash.html",{"contact":contact})
    
    def post(self, request):
        contact = Contactinfo.objects.all().first()
        if contact:
            form = ContactForm(request.POST, instance=contact)
            if form.is_valid():
                form.save()
                messages.success(request, "Contact info updated successfully!")
                return redirect("admindashboard")
            else:
                messages.error(request, "Invalied fields")
                return redirect("admindashboard")

        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Contact info updated successfully!")
                return redirect("admindashboard")
            else:
                messages.error(request, "Invalied fields")
                return redirect("admindashboard")


class adminplans(LoginRequiredMixin,View):
    def get(self, request):
        plans = Plans.objects.all()
        return render(request, "plan.html", {"plans": plans})
    

class QuestionsView(LoginRequiredMixin,View):
    def get(self, request):
        questions = Questions.objects.all()
        return render(request, "questions.html", {"questions":questions})
    
    def post(self, request):
        id = request.POST.get("id")
        question = Questions.objects.get(id=id)
        if question:
            form = QuestionForm(request.POST, instance=question)
            if form.is_valid():
                form.save()
                return redirect("adminquestions")
            else:
                messages.error(request, "Invalied fields")
                return redirect("adminquestions")
        else:
            messages.error(request, "Question not found!")
            return redirect("adminquestions")
        
class SubmitQuestion(LoginRequiredMixin,View):
    
    def post(self, request):
        print("submit qst", request.POST)
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("adminquestions")

class SubmitPlan(LoginRequiredMixin,View):
    def post(self, request):
        data = request.POST
        form = PlanForm(request.POST)
        if form.is_valid():
            pln_obj = form.save()
            deactive_features = json.loads(data.get("deactive_fetures"))
            active_features = json.loads(data.get("active_fetures"))

            for ftr in deactive_features:
                PlanFeatures.objects.create(plan=pln_obj, feature_description=ftr, is_active=False)
            for ftr in active_features:
                PlanFeatures.objects.create(plan=pln_obj, feature_description=ftr, is_active=True)
        return redirect("adminplans")

class DeletePlan(LoginRequiredMixin,View):
    def post(self, request):
        id = request.POST.get("plan_id")
        plan = Plans.objects.get(id=id)
        if plan:
            plan.delete()
        return redirect("adminplans")

class DeleteQuestion(LoginRequiredMixin,View):
    def post(self, request):
        id = request.POST.get("id")
        question = Questions.objects.get(id=id)
        if question:
            question.delete()
        return redirect("adminquestions")
    
