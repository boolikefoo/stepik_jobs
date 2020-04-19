from django.contrib import admin
from .models import Company, Specialty, Vacancy

# Register your models here.

class AdminCompany(admin.ModelAdmin):
    pass


class AdminSpecialty(admin.ModelAdmin):
    pass


class AdminVacancy(admin.ModelAdmin):
    pass


admin.site.register(Company, AdminCompany)
admin.site.register(Specialty, AdminSpecialty)
admin.site.register(Vacancy, AdminVacancy)
