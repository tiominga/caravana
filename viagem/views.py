from django.shortcuts import render
from .models import Viagem


# Create your views here.
def viagem_index(request):
    return render(request, 'viagem_index.html')

def viagem_form(request):
    return render(request, 'viagem_form.html')

def viagem_save(request):
    return render(request, 'viagem_save.html')

def viagem_find(request):
    return render(request, 'viagem_find.html')
