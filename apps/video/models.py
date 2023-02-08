from django.db import models
from apps.company.models import Company

# Create your models here.

class Video(models.Model):
    name=models.CharField(max_length=120,verbose_name='Название')
    date=models.DateField(verbose_name='Дата')
    company= models.ForeignKey(Company, on_delete=models.CASCADE,
    related_name='videos',verbose_name='Компания-Организатор')
    description=models.TextField(verbose_name='Описание')
    video=models.FileField(upload_to='/video/video/',verbose_name='Видео')
    email=models.EmailField('Почта')

 

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Видео'
        verbose_name_plural='Видео'

