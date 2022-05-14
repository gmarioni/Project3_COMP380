from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Issues
from .forms import IssuesForm
import issuesApp.issues as ifunc

# Create your views here.
def main(request):
    list = Issues.objects.all()
    context = {"issues":list}
    return render(request,'issuesApp/issues.html', context)

def item(request,pk):
    tobj = Issues.objects.get(id=pk)
    context = {"issue": tobj,"actionitems":ifunc.getAssociatedActionItems(pk),
                "decisions":ifunc.getAssociatedDecisions(pk)}
    return render(request,'issuesApp/issue.html', context)

def create(request):
    form = IssuesForm
    if request.method == 'POST':
        ifunc.createIssues(request.POST)
        return redirect('issues')
    context = {'form':form}
    return render(request, 'issuesApp/issues_form.html', context)

def update(request,pk):
    issue = Issues.objects.get(id=pk)
    form = IssuesForm(instance=issue)
    if request.method == 'POST':
        ifunc.updateIssues(issue, request.POST)
        return redirect('issue',pk)
    context = {'form':form}
    return render(request, 'issuesApp/issues_form.html', context)

def delete(request,pk):
    issue = Issues.objects.get(id=pk)
    if request.method == 'POST':
        issue.delete()
        return redirect('issues')
    context = {'obj':issue}
    return render(request, 'delete.html', context)