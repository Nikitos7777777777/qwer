from django.urls import path
from . import views
from Sait.views import home

urlpatterns = [
    path('',views.home, name = "home"),
    path("signup/",views.SignUp.as_view(),name="signup"),
]