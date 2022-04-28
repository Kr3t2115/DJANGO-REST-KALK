from django.urls import path
from . import views

urlpatterns = [
  path('obliczenia/', views.ShowAll, name='obliczenia'),
]