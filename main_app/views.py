from django.shortcuts import render
from django.http import HttpResponse
from .models import Finch

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def finches_index(request):
    finches = Finch.objects.order_by('name')
    return render(request, 'finches/index.html', {'finches': finches})  

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})      