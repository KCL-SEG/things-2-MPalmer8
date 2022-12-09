from django.shortcuts import render
from .forms import ThingForm

def home(request):
    return render(request, 'home.html', {'form': form})

def things(request):
    form = ThingForm()
    return render(request, 'home.html', {'form': form})
