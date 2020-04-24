from .data import *

''' компании '''

for _ in companies:
    Company.objects.create(
        name = _['title']
    )

''' компании '''

for _ in specialties:
    Specialty.objects.create(
        code = _['code'],
        title = _['title']

    )

''' Вакансии '''

for _ in jobs:
    spec = Specialty.objects.filter(code = _['cat']).first()
    comp = Company.objects.filter(name = _['company']).first()
    Vacancy.objects.create(
        title = _['title'],
        specialty = spec,
        company = comp,
        salary_min = _['salary_from'],
        salary_max = _['salary_to'],
        published_at = _['posted']
        )