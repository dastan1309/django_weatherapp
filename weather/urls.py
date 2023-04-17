
from django.urls import path
import weather
from weather import views

urlpatterns = [

    path('', views.index),
]
