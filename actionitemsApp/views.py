from django.http import HttpResponse
from django.shortcuts import render, redirect
import actionitemsApp.actionitems as aifunc
from .models import Actionitems
from .forms import ActionitemsForm


# Create your views here.
def main(request):
    objs = Actionitems.objects.all()
    context = {"actionitems":objs}
    return render(request,'actionitemsApp/actionitems.html', context)

def item(request,pk):
    obj = Actionitems.objects.get(id=pk)
    context = {"actionitem": obj}
    return render(request,'actionitemsApp/actionitem.html', context)

def create(request):
    form = ActionitemsForm
    if request.method == 'POST':
        aifunc.createActionitems(request.POST)
        return redirect('actionitems')
    context = {'form':form}
    print(form)
    return render(request, 'actionitemsApp/actionitem_form.html', context)

def update(request,pk):
    obj = Actionitems.objects.get(id=pk)
    form = ActionitemsForm(instance=obj)
    if request.method == 'POST':
        aifunc.updateActionitems(obj, request.POST)
        return redirect('actionitem',pk)
    context = {'form':form}
    return render(request, 'actionitemsApp/actionitems_form.html', context)

def delete(request,pk):
    obj = Actionitems.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('actionitems')
    context = {'obj':obj}
    return render(request, 'delete.html', context)