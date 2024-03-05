from django.shortcuts import render, HttpResponseRedirect
from .forms import new
from .models import User

# Create your views here.

#This  function will add new items and show them.
def add_new(request):
    if request.method == 'POST':
        fm = new(request.POST)
        if fm.is_valid():
            tk = fm.cleaned_data['task']
            dc = fm.cleaned_data['description']
            reg = User(task=tk, description=dc)
            reg.save()
            fm = new()
    else:
            fm = new()
    stud = User.objects.all()        
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})  

#This function will update new items 
def update_data(request,id):
     if request.method == 'POST':
          pi = User.objects.get(pk=id)
          fm = new(request.POST,instance=pi)
          if fm.is_valid():
               fm.save()
     else:
          pi = User.objects.get(pk=id)
          fm = new(instance=pi)
     return render(request,'enroll/update.html',{'form':fm})                     

#This function will delete items.
def delete_data(request,id):
     if request.method == 'POST':
          pi = User.objects.get(pk=id)
          pi.delete()
          return HttpResponseRedirect('/')

