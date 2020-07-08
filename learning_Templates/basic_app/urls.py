from django.conf import Path
from basic_app import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
