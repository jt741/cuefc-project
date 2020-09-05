from django.urls import path
from . import views

urlpatterns = [
    path('', views.allnews, name='about'),
    path('clubnews/', views.teamnews, name='teamnews'),
    path('committee/', views.committee, name='committee'),
    path('sponsorship/', views.sponsorship, name='sponsors'),
    path('<int:newspost_id>/', views.newsdetail, name='newsdetail'),
    path('thecaptains/', views.captains, name='captains'),
    path('docs/', views.docs, name='docs'),
]