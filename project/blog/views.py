from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'pages/home.html')
def contract(request):
    return render(request, 'pages/contract.html')
def error(request,exception=None):
    return render(request, 'pages/error.html', status = 404)
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})