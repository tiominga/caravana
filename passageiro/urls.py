"""
URL configuration for caravana project.

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
from django.urls import path
from . import views

app_name = 'passageiro'

urlpatterns = [
       path('delete/<int:id>/', views.passageiro_delete, name='delete'),      
       path('form/',views.passageiro_form,name='form'),
       path('form/<int:id>/', views.passageiro_form, name='form_edit'),
       path('save/',views.passageiro_save,name='save'),      
]
