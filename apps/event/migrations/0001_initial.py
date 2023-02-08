# Generated by Django 4.1.5 on 2023-02-08 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата проведения')),
                ('image', models.ImageField(upload_to='event/image', verbose_name='Фото')),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('location', models.CharField(max_length=120, verbose_name='Локация')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='company.company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]