from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Toy
from .forms import FeedingForm

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
    feeding_form = FeedingForm()
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=finch.toys.all().values_list('id'))
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'toys': toys_finch_doesnt_have
        })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('finches_detail', finch_id = finch_id)   

def assoc_toy(request, finch_id, toy_id):
    finch = Finch.objects.get(id=finch_id)
    finch.toys.add(toy_id)
    return redirect('finches_detail', finch_id = finch_id)                

#using imported CreateView we can now create our our class based view function to create finch
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['color', 'species']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'        

class ToyList(ListView):
    model = Toy
    fields ='__all__'

class ToyDetail(DetailView):
    model = Toy


class ToyCreate(CreateView):
    model = Toy 
    fields= '__all__'  
     

class ToyUpdate(UpdateView) :
    model: Toy
    fields='__all__'
    # succes_url ='/toys/'   