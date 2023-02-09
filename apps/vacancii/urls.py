from rest_framework.routers import DefaultRouter as DR
from apps.vacancii.views import VacanciiView

router=DR()

router.register('vacancii',VacanciiView, basename= 'vacancii')

urlpatterns=[]

urlpatterns += router.urls
