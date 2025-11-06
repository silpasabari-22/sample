"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.reg,name='reg'),
    path('login',views.Login,name='login'),
    path('userhome',views.userhome,name='userhome'),
    path('Profile',views.Profile,name='Profile'),
    path('reset',views.password_reset_request,name='reset'),
    path('verify',views.verify_otp,name='verify'),
    path('set_new_password',views.set_new_password,name='set_new_password'),
    
]

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_rooot=settings.MEDIA_ROOT)
