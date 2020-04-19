from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import jobs.models



# Create your models here.
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

    user = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    status = models.CharField(max_length=3, choices=status_coices, default='LFJ')
    salary = models.PositiveIntegerField()
    specialty = models.CharField(max_length=64)
    grade = models.CharField(max_length=2, choices=grade_choices, default='tr')
    educaation = models.TextField()
    experience = models.TextField()
    portfolio = models.TextField()

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
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
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=64)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey('jobs.Vacancy', on_delete=models.CASCADE, related_name='application')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='application')

    def __str__(self):
        return self.written_username
    