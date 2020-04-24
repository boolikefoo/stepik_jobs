from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import jobs.models



# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.user.id}/{filename}'

class Resume(models.Model):    
    status_coices = (
        ('DFJ', 'Не ищу работу'),
        ('LO', 'Рассматриваю предложения'),
        ('LFJ','Ищу работу'),
    )

    grade_choices = (
        ('tr','Стажёр'),
        ('jn', 'Джуниор'),
        ('md', 'Мидл'),
        ('sn', 'Синьор'),
        ('ld', 'Лид'),
    )

    user = models.CharField(max_length=64, verbose_name='Пользователь')
    name = models.CharField(max_length=64, verbose_name='Имя')
    surname = models.CharField(max_length=64, verbose_name='Фамилия')
    status = models.CharField(max_length=3, choices=status_coices, default='LFJ', verbose_name='Статус')
    salary = models.PositiveIntegerField(verbose_name='Зарплата')
    specialty = models.CharField(max_length=64, verbose_name='Специализация')
    grade = models.CharField(max_length=2, choices=grade_choices, default='tr', verbose_name='Уровень')
    education = models.TextField(default=None, null=True, verbose_name='Образование')
    experience = models.TextField(default=None, null=True, verbose_name='Опыт работы')
    portfolio = models.FileField(upload_to='user_directory_path', verbose_name='Портфолио')

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name='Имя')
    surname = models.CharField(max_length=64, verbose_name='Фамилия')
    company = models.CharField(max_length=64, verbose_name='Компания')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='myuser')

    def __str__(self):
        return self.name
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):    
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Application(models.Model):
    written_username = models.CharField(max_length=64, verbose_name='Автор')
    written_phone = models.CharField(max_length=64, verbose_name='Телефон автора')
    written_cover_letter = models.TextField(verbose_name='Сопроводительное письмо')
    vacancy = models.ForeignKey('jobs.Vacancy', on_delete=models.CASCADE, related_name='application', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='application')

    def __str__(self):
        return self.written_username
    