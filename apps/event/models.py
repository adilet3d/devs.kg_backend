from django.db import models
from apps.company.models import Company
# Create your models here.
class Event(models.Model):
    date=models.DateTimeField(verbose_name='Дата проведения')
    image=models.ImageField(upload_to='event/image',
    verbose_name='Фото')
    company=models.ForeignKey(Company,on_delete= models.CASCADE,
    related_name='events',verbose_name='Компания')
    name=models.CharField(max_length=120,verbose_name='Название')
    location=models.CharField(max_length=120,verbose_name='Локация')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Мероприятие'
        verbose_name_plural= 'Мероприятия'

