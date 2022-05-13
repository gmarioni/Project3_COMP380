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
        dfunc.createIssues(request.POST)
        return redirect('decisions')
    context = {'form':form}
    return render(request, 'decisionsApp/decision_form.html', context)

# def update(request,pk):
#     issue = Issues.objects.get(id=pk)
#     form = IssuesForm(instance=issue)
#     if request.method == 'POST':
#         ifunc.updateIssues(issue, request.POST)
#         return redirect('issue',pk)
#     context = {'form':form}
#     return render(request, 'issuesApp/issues_form.html', context)

# def delete(request,pk):
#     issue = Issues.objects.get(id=pk)
#     if request.method == 'POST':
#         issue.delete()
#         return redirect('issues')
#     context = {'obj':issue}
#     return render(request, 'delete.html', context)