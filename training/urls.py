from django.urls import path
from . import views

urlpatterns = [
    path('', views.training, name='training'),
    path('beginners/', views.beginners, name='beginners'),
    path('matchcalendar', views.calendar, name='calendar'),
]