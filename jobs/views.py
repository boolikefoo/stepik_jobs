from django.db import models
from django.views import View
from django.shortcuts import render
from jobs.models import Company, Specialty, Vacancy


context = {'text': 'some text here'}

class MainView(View):
    specialties = Specialty.objects.all()
    context.update({'spetialties' : specialties })
    print(context)
    def get(self, request):
        return render(request, 'index.html', context=(context))


class VacanciesView(View):
    def get(self, request):
        return render(request, 'list.html', context=(context))


class CompaniesView(View):
    def get(self, request, id):
        return render(request, 'company.html', context=(context))    


class JobsView(View):
    def get(self, request, id):
        return render(request, 'vacancy.html', context=(context))    


class CatalogView(View):
    def get(self, request, specialty):
        return render(request, 'vacancy-list.html', context=(context))                            