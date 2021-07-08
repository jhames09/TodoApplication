from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *


# Create your views here.
def index(request):
     all_item = TodoItem.objects.all()
    
     form = TodolistForm()
     if request.method == 'POST':
         form = TodolistForm(request.POST)
         if form.is_valid():
             form.save()
         return redirect('/')

     context = {'all_item': all_item, 'form': form}
     return render(request, 'todo/index.html', context)

def updatelist(request, pk):
    item = TodoItem.objects.get(id=pk)
    form = TodolistForm(instance=item)

    if request.method == "POST":
        form = TodolistForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')


    context = {'form': form}
    return render(request, 'todo/update.html', context)


def deleteTodo(request, pk):
    item = TodoItem.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'todo/delete.html', context)




