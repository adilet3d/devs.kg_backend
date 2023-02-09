from rest_framework.routers import DefaultRouter as DR
from apps.event.views import EventView

router=DR()

router.register('event',EventView, basename= 'event')

urlpatterns=[]

urlpatterns += router.urls