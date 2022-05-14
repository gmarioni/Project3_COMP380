from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Deliverables
from .forms import DeliverablesForm
import deliverablesApp.deliverables as dfunc

# Create your views here.
def main(request):
    list = Deliverables.objects.all()
    context = {"deliverables":list}
    return render(request,'deliverablesApp/deliverables.html', context)

def item(request,pk):
    obj = Deliverables.objects.get(id=pk)
    context = {"deliverable": obj,"tasks":dfunc.getAssociatedTasks(fk_id=pk)}
    return render(request,'deliverablesApp/deliverable.html', context)

def create(request):
    form = DeliverablesForm
    if request.method == 'POST':
        dfunc.createDeliverable(request.POST)
        return redirect('deliverables')
    context = {'form':form}
    return render(request, 'deliverablesApp/deliverable_form.html', context)

def update(request,pk):
    deliverable = Deliverables.objects.get(id=pk)
    form = DeliverablesForm(instance=deliverable)
    if request.method == 'POST':
        dfunc.updateDeliberable(deliverable,request.POST)
        return redirect('deliverables')
    context = {'form':form}
    return render(request, 'deliverablesApp/deliverable_form.html', context)

def delete(request,pk):
    deliverable = Deliverables.objects.get(id=pk)
    if request.method == 'POST':
        deliverable.delete()
        return redirect('deliverables')
    context = {'obj':deliverable}
    return render(request, 'deliverablesApp/delete.html', context)