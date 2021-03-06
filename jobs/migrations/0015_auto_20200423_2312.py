# Generated by Django 3.0.5 on 2020-04-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_auto_20200419_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(verbose_name='Описание компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='employee_count',
            field=models.IntegerField(null=True, verbose_name='Количество сотрудников'),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=64, verbose_name='Местонахождение'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(height_field='height_field', upload_to='company_logo', verbose_name='Логотип компании', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='code',
            field=models.CharField(max_length=64, verbose_name='Язык программирования'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(upload_to='specialty_pictures', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.PositiveIntegerField(verbose_name='Максимальная зарплата'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.PositiveIntegerField(verbose_name='Минимальная зарплата'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.CharField(max_length=64, verbose_name='Навыки'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Заголовок'),
        ),
    ]
