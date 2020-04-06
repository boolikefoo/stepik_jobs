from django.db import models

# Create your models here.

class Vacancy(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='')
    company = models.CharField(max_length=64)
    skills = models.CharField(max_length=64)
    description = models.TextField( )
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateTimeField()


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.CharField(default=None, null=True)
    description = models.TextField()
    employee_count = models.IntegerField()


class Specialty(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.CharField(default=None, null=True)
    