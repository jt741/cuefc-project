from django.urls import path
from . import views

urlpatterns = [
    path('', views.allnews, name='allnews'),
    path('clubnews/', views.teamnews, name='teamnews'),
    path('committee/', views.committee, name='committee'),
    path('sponsership/', views.sponsership, name='sponsers'),
    path('<int:newspost_id>/', views.newsdetail, name='newsdetail')
]