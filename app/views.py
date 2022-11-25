from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from app.models import account
from app.forms import accountform

# Create your views here.


def index(request):
    form = accountform()
    if request.method == 'POST':
        form = accountform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'app/index.html',{'form':form})