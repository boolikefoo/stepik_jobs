"""stepik_jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth.views import LogoutView

from jobs.views import MainView, VacancyListView, CompanyView, JobView, SpecialtiesView, JobSendView, SearchView
from account.views import MyResumeView, MyCompanyView, MyResumeView, MyVacanciesView, MyVacancyView, UserLoginView, UserSignupView


urlpatterns = [
    path('', MainView.as_view(), name="main"),
    path('vacancies/', VacancyListView.as_view(), name="vacancies"),
    path('companies/<int:id>/', CompanyView.as_view(), name="companies"),
    path('jobs/<int:id>/', JobView.as_view(), name="job"),
    path('jobs/cat/<str:specialty_>/', SpecialtiesView.as_view(), name="specialty_url"),
    path('jobs/<int:id>/send', JobSendView.as_view(), name='send'),
    
    path('myresume/', MyResumeView.as_view(), name='myresume'),
    path('mycompany', MyCompanyView.as_view(), name='mycompany'),
    path('mycompany/vacancies/', MyVacanciesView.as_view(), name='myvacancies'),
    path('mycompany/vacancies/<int:id>', MyVacancyView.as_view(), name='myvacancy'),
    path('search/', SearchView.as_view(), name='search'),

    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)