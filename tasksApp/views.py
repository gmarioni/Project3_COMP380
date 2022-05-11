from django.http import HttpResponse
from django.shortcuts import render, redirect
from deliverablesApp.models import Deliverables
from .models import Tasks
from .forms import TasksForm

# Create your views here.
def main(request):
    list = Tasks.objects.all()
    context = {"tasks":list}
    return render(request,'tasksApp/tasks.html', context)

def item(request,pk):
    tobj = Tasks.objects.get(task_id=pk)
    dobj = Deliverables.objects.get(deliverable_id=tobj.deliverable_id)
    context = {"task": tobj,"deliverable":dobj}
    return render(request,'tasksApp/task.html', context)

def create(request):
    form = TasksForm
    if request.method == 'POST':
        form = TasksForm(request.POST)
        form.save()
        return redirect('')
    context = {'form':form}
    return render(request, 'tasksApp/tasks_form.html', context)

def update(request,pk):
    deliverable = Tasks.objects.get(task_id=pk)
    form = TasksForm(instance=deliverable)
    if request.method == 'POST':
        form = TasksForm(request.POST, instance=deliverable)
        form.save()
        return redirect('')
    context = {'form':form}
    return render(request, 'tasksApp/tasks_form.html', context)

def delete(request,pk):
    deliverable = Tasks.objects.get(deliverable_id=pk)
    if request.method == 'POST':
        deliverable.delete()
        return redirect('')
    context = {'obj':deliverable}
    return render(request, 'tasksApp/delete.html', context)