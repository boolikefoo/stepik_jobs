from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name='Название компании')
    location = models.CharField(max_length=64, verbose_name='Местонахождение')
    logo = models.ImageField(upload_to='company_logo', height_field='height_field', width_field='width_field', verbose_name='Логотип компании')
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)
    description = models.TextField(verbose_name='Описание компании')
    employee_count = models.IntegerField(null=True, verbose_name='Количество сотрудников')
    
    def __str__(self):
        return self.name
    


class Specialty(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=64, verbose_name='Язык программирования')
    title = models.CharField(max_length=64, verbose_name='Специализация')
    picture = models.ImageField(upload_to='specialty_pictures', verbose_name='Изображение')

    def __str__(self):
        return self.title
    


class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='job_specialty')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=64, verbose_name='Навыки')
    description = models.TextField(verbose_name='Описание')
    salary_min = models.PositiveIntegerField(verbose_name='Минимальная зарплата')
    salary_max = models.PositiveIntegerField(verbose_name='Максимальная зарплата')
    published_at = models.DateTimeField(auto_now_add=True)
    applications = models.ForeignKey('account.Application', on_delete=models.CASCADE, related_name='applications' )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.title
    