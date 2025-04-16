from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
def home_index(request):
    return render(request, 'home/index.html')

def home_organizador(request):    
    request.session['eh_organizador'] = 1   
    return redirect('/accounts/login/')

def home_dashboard(request):
    if request.session.get('eh_organizador') == 1:
        return render(request, 'home/organizador.html')
    else:
        return render(request, 'home/passageiro.html')
                  