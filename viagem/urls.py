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

app_name = 'viagem'

urlpatterns = [
       path('delete/<int:id>/', views.viagem_delete, name='delete'),
       path('',views.viagem_index,name='index'),
       path('form/',views.viagem_form,name='form'),
       path('form/<int:id>/', views.viagem_form, name='form_edit'),
       path('save/',views.viagem_save,name='save'),
       path('list_all/',views.viagem_list_all,name='list_all'),
       path('find/',views.viagem_find,name='find'),
       path('origem_options/',views.viagem_origem_options,name='origem_options'),
       path('destino_options/',views.viagem_destino_options,name='destino_options'),
       path('query_find',views.viagem_sql_find,name='query_find')

]
