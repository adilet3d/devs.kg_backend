
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions



urlpatterns2 = [
    path('company/' ,include ('apps.company.urls')),
    path('event/' ,include ('apps.event.urls')),
    path('vacancy/' ,include ('apps.vacancii.urls')),
    path('video/' ,include ('apps.video.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('rest_framework.urls')),
    path('api/', include(urlpatterns2))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)