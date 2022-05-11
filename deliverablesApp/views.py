from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Deliverables
from .forms import DeliverablesForm

# Create your views here.
def main(request):
    list = Deliverables.objects.all()
    context = {"deliverables":list}
    return render(request,'deliverablesApp/deliverables.html', context)

def item(request,pk):
    obj = Deliverables.objects.get(deliverable_id=pk)
    context = {"deliverable": obj}
    return render(request,'deliverablesApp/deliverable.html', context)

def create(request):
    form = DeliverablesForm
    if request.method == 'POST':
        form = DeliverablesForm(request.POST)
        form.save()
        return redirect('')
    context = {'form':form}
    return render(request, 'deliverablesApp/deliverable_form.html', context)

def update(request,pk):
    deliverable = Deliverables.objects.get(deliverable_id=pk)
    form = DeliverablesForm(instance=deliverable)
    if request.method == 'POST':
        form = DeliverablesForm(request.POST, instance=deliverable)
        form.save()
        return redirect('')
    context = {'form':form}
    return render(request, 'deliverablesApp/deliverable_form.html', context)

def delete(request,pk):
    deliverable = Deliverables.objects.get(deliverable_id=pk)
    if request.method == 'POST':
        deliverable.delete()
        return redirect('')
    context = {'obj':deliverable}
    return render(request, 'deliverablesApp/delete.html', context)