from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Decisions
from .forms import DecisionsForm
import decisionsApp.decisions as dfunc

# Create your views here.
def main(request):
    obj = Decisions.objects.all()
    context = {"decisions":obj}
    return render(request,'decisionsApp/decisions.html', context)

def item(request,pk):
    obj = Decisions.objects.get(id=pk)
    context = {"decision": obj}
    return render(request,'decisionsApp/decision.html', context)

def create(request):
    form = DecisionsForm
    if request.method == 'POST':
        dfunc.createDecisions(request.POST)
        return redirect('decisions')
    context = {'form':form}
    return render(request, 'decisionsApp/decision_form.html', context)

def update(request,pk):
    decision = Decisions.objects.get(id=pk)
    form = DecisionsForm(instance=decision)
    if request.method == 'POST':
        dfunc.updateDecisions(decision, request.POST)
        return redirect('decision',pk)
    context = {'form':form}
    return render(request, 'decisionsApp/decision_form.html', context)

def delete(request,pk):
    decision = Decisions.objects.get(id=pk)
    if request.method == 'POST':
        decision.delete()
        return redirect('decision')
    context = {'obj':decision}
    return render(request, 'delete.html', context)