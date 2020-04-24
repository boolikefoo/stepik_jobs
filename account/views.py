from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

context = {'some' : 'asddsa'}

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class UserSignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'register.html'


class MyResumeView(View):
    def get(self, request):
        return render(request, 'resume-edit.html', context=context)

class MyCompanyView(View):
    def get(self, request):
        return render(request, 'company-edit.html', context=context)


class MyVacanciesView(View):
    def get(self, request):
        return render(request, 'vacancy-list.html', context=context)


class MyVacancyView(View):
    def get(self, request, id):
        return render(request, 'vacancy-edit', context=context)