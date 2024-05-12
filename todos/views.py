from django.shortcuts import render, redirect

from todos.forms import taskform
from todos.models import task


# Create your views here.

def dash(request):
    return render(request,'dash.html')

def addtask(request):
    form = taskform()
    u = request.user
    if request.method == 'POST':
        form = taskform(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
        return redirect('viewtask')
    return render(request,'addtask.html',{'form':form})

def viewtask(request):
    data = task.objects.all()
    return render(request,'viewtask.html',{'data':data})

def taskupdate(request,id):
    user = task.objects.get(id=id)
    form = taskform(instance=user)
    if request.method == "POST":
        form = taskform(request.POST or None, request.FILES, instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('viewtask')
    return render(request, 'taskupdate.html', {'form': form})


def taskdelete(request,id):
    data=task.objects.get(id=id)
    data.delete()
    return redirect('viewtask')
