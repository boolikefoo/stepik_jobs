from django.db import models
from django.views import View
from django.shortcuts import render
from django.db.models import Count
from django.template.defaulttags import register
from jobs.models import Company, Specialty, Vacancy
import pymorphy2


context = {}

@register.filter
def morphyF(number, word):
    '''Согласование слов с числительными'''
    morph = pymorphy2.MorphAnalyzer()
    morphy = morph.parse(word)[0]
    new_word = morphy.make_agree_with_number(number).word

    return new_word


class MainView(View):
    def get(self, request):
        context.update({
            'spetialties' : Specialty.objects.all().annotate(cnt = Count('job_specialty')),
            'companies' : Company.objects.all().annotate(cnt = Count('vacancies')),
            })

        return render(request, 'index.html', context=(context))


class VacancyListView(View):
    context.update({'vacancies' : Vacancy.objects.all(), }) 

    def get(self, request):
        return render(request, 'list.html', context=(context))


class SpecialtiesView(View):
    def get(self, request, specialty_):
        title = Specialty.objects.filter(code=specialty_).first()
        context.update({'specialties' : Vacancy.objects.filter(specialty__code=specialty_), 'title' : title}) 
        return render(request, 'specialties-list.html', context=(context))


class CompanyView(View):
    def get(self, request, id):
        company = Company.objects.get(id=id)
        context.update({'company' : company, 'vacancies' : Vacancy.objects.filter(company=company.id),})        
        return render(request, 'company.html', context=(context))    


class JobView(View):
    def get(self, request, id):
        context.update({'job' : Vacancy.objects.get(id=id)})
        return render(request, 'vacancy.html', context=(context))    


class JobSendView(View):
    def post(self, request):
        return render(request, '') 
                    