
from django.urls import path, include
from .views import HomeView, BuisinessView, eventsView, franchiseView, privacypolicyView, termsandconditionsView, adminlogin, admindashboard, adminplans, QuestionsView, SubmitQuestion, DeleteQuestion, SubmitPlan, DeletePlan, AdminLogout

urlpatterns = [
    path("", HomeView.as_view()),
    path("business/", BuisinessView.as_view(), name="business"),
    path("events/", eventsView.as_view(), name="events"),
    path("franchise/", franchiseView.as_view(), name="franchise"),
    path("privacypolicy/", privacypolicyView.as_view(), name="privacypolicy"),
    path("termsandconditions/", termsandconditionsView.as_view(), name="termsandconditions"),
    
    # admin
    path("administration/login", adminlogin.as_view(), name="adminlogin"),
    path("administration/dash", admindashboard.as_view(), name="admindashboard"),
    path("administration/plans", adminplans.as_view(), name="adminplans"),
    path("administration/questions", QuestionsView.as_view(), name="adminquestions"),
    path("administration/submit-question", SubmitQuestion.as_view(), name="submit-question"),
    path("administration/delete-question", DeleteQuestion.as_view(), name="delete-question"),
    path("administration/submit-plan", SubmitPlan.as_view(), name="submit-plan"),
    path("administration/delete-plan", DeletePlan.as_view(), name="delete-plan"),
    path("administration/AdminLogout", AdminLogout.as_view(), name="adminlogout")
    
]
