from django.shortcuts import render

  

# Create your views here.
def viagem_index(request):
    return render(request, 'viagem_index.html')

def viagem_form(request):
    return render(request, 'viagem_form.html')

def viagem_add(request):
    return render(request, 'viagem_add.html')

def viagem_find(request):
    return render(request, 'viagem_find.html')
