from django.db import models

# Create your models here.
class Company(models.Model):
    logo= models.ImageField(upload_to='company/logo/',verbose_name='Логотип')
    name= models.CharField(max_length=120, verbose_name='Название')
    description=models.TextField(verbose_name='Описание')
    telegram=models.URLField(verbose_name='Телега')
    whatsapp=models.URLField(verbose_name='Вотсапп')

    @property 
    def vacancii_count(self):
        return self.vacancii.count()
    
    @property
    def event_amount(self):
        return self.event.count()
    @property
    def video_amount(self):
        return self.videos.count()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name='Компания'
        verbose_name_plural='Компании'