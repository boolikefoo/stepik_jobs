from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    pass


class UserSignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'register.html'


class MyResumeView(View):
    pass


class MyCompanyView(View):
    pass


class MyVacanciesView(View):
    pass


class MyVacancyView(View):
    pass