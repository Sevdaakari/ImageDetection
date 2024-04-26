from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('success/', views.success, name='success'),
    path('objects_not_detected/', views.objects_not_detected, name='objects_not_detected'),
    
]
