from django.http import HttpResponse
from django.shortcuts import render, redirect
from deliverablesApp.models import Deliverables
from issuesApp.models import Issues
from .models import Tasks
from .forms import TasksForm
import tasksApp.tasks as tfunc

# Create your views here.
def main(request):
    list = Tasks.objects.all()
    context = {"tasks":list}
    return render(request,'tasksApp/tasks.html', context)

def item(request,pk):
    tobj = Tasks.objects.get(id=pk)
    context = {"task": tobj, "issues":tfunc.getAssociatedIssues(fk_id=pk)}
    return render(request,'tasksApp/task.html', context)

def create(request):
    form = TasksForm
    if request.method == 'POST':
        tfunc.createTasks(request.POST)
        return redirect('tasks')
    context = {'form':form}
    return render(request, 'tasksApp/tasks_form.html', context)

def update(request,pk):
    task = Tasks.objects.get(id=pk)
    form = TasksForm(instance=task)
    if request.method == 'POST':
        tfunc.updateTasks(task,request.POST)
        return redirect('tasks')
    context = {'form':form}
    return render(request, 'tasksApp/tasks_form.html', context)

def delete(request,pk):
    task = Tasks.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    context = {'obj':task}
    return render(request, 'delete.html', context)