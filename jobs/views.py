from django.db import models
from django.db.models import Count
from django.views import View
from django.shortcuts import render
from jobs.models import Company, Specialty, Vacancy
import pymorphy2


context = {}

def morphyF(word, number):
    '''Согласование слов с числительными'''
    morph = pymorphy2.MorphAnalyzer()
    morphy = morph.parse(word)[0]
    new_word = morphy.make_agree_with_number(number).word

    return new_word


class MainView(View):
    context.update({'spetialties' : Specialty.objects.all(), 'companies' : Company.objects.all(),})

    def get(self, request):
        return render(request, 'index.html', context=(context))


class VacancyListView(View):
    morphy = morphyF('вакансия', Vacancy.objects.all().count())
    context.update({'vacancies' : Vacancy.objects.all(), 'morphy' : morphy}) 

    def get(self, request):
        return render(request, 'list.html', context=(context))


class SpecialtiesView(View):
    def get(self, request, specialty_):
        title = Specialty.objects.filter(code=specialty_).first()
        morphy = morphyF('вакансия', Vacancy.objects.filter(specialty__code=specialty_).count())
        context.update({'specialties' : Vacancy.objects.filter(specialty__code=specialty_), 'morphy' : morphy, 'title' : title}) 
        return render(request, 'specialties-list.html', context=(context))


class CompanyView(View):
    def get(self, request, id):
        company = Company.objects.get(id=id)
        morphy = morphyF('вакансия', Vacancy.objects.filter(company=company.name).count())
        context.update({'company' : company, 'vacancies' : Vacancy.objects.filter(company=company.name), 'morphy' : morphy})        
        return render(request, 'company.html', context=(context))    


class JobView(View):
    def get(self, request, id):
        context.update({'job' : Vacancy.objects.get(id=id)})
        return render(request, 'vacancy.html', context=(context))    
                    