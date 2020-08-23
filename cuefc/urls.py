"""cuefc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



admin.site.site_header = "CUEFC Admin"
admin.site.site_title = "CUEFC Admin Portal"
admin.site.index_title = "Welcome to the CUEFC Admin Page"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html/', views.home, name='home'),
    path('contact/', views.contactus, name='contactus'),
    path('supportus/', views.donate, name='donate'),
    path('about/', include('teamnews.urls')),
    path('gallery/', include('gallery.urls')),
    path('trainingandmatches/', include('training.urls')),
    path('donors/', views.contactus, name='contactus'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
