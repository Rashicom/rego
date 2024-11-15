
from django.urls import path, include
from .views import HomeView, BuisinessView, eventsView, franchiseView, privacypolicyView, termsandconditionsView

urlpatterns = [
    path("", HomeView.as_view()),
    path("business/", BuisinessView.as_view(), name="business"),
    path("events/", eventsView.as_view(), name="events"),
    path("franchise/", franchiseView.as_view(), name="franchise"),
    path("privacypolicy/", privacypolicyView.as_view(), name="privacypolicy"),
    path("termsandconditions/", termsandconditionsView.as_view(), name="termsandconditions"),

]
