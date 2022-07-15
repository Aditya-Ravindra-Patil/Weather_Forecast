from django.urls import path, include
from weather_app import views

urlpatterns = [
    path('',views.home, name='home')
]
