"""
URL configuration for cards project.

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reqq',views.fun3,name='reqq'),
    path('dataa',views.dataview,name='dataa'),
    path('vieww',views.data,name='vieww'),
    path('card',views.dataview,name='card'),
    path('delete/<int:id>/', views.delete_student, name='delete'),
    path('edit/<int:id>/',views.edit_student,name='edit'),
]