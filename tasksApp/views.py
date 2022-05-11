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
    tobj = Tasks.objects.get(id=pk)
    #dobj = Deliverables.objects.get(id=tobj.deliverable_id)
    context = {"task": tobj}
    return render(request,'tasksApp/task.html', context)

def create(request):
    form = TasksForm
    if request.method == 'POST':
        form = TasksForm(request.POST)
        print(request.POST)
        form.save()
        return redirect('tasks')
    context = {'form':form}
    return render(request, 'tasksApp/tasks_form.html', context)

def update(request,pk):
    task = Tasks.objects.get(id=pk)
    form = TasksForm(instance=task)
    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        form.save()
        return redirect('tasks')
    context = {'form':form}
    return render(request, 'tasksApp/tasks_form.html', context)

def delete(request,pk):
    task = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    context = {'obj':task}
    return render(request, 'tasksApp/delete.html', context)