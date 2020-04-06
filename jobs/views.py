from django.views import View
from django.shortcuts import render

# Create your views here.

context = {}

class MainView(View):
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