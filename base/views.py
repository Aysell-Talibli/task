from django.shortcuts import render, redirect
from selenium import webdriver
from .forms import InstagramForm, Add_intagramForm
from automation_w_selenium.tasks import login_to_instagram, find_counts
from .models import InstagramModel

def home(request):
    user_data=InstagramModel.objects.all()
    return render(request,'home.html',{'user_data':user_data})


def add_instagram(request):
    if request.method=='POST':
        form=InstagramForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login_to_instagram(username, password)
            return redirect('home')
    else:
        form=InstagramForm()
    return render(request, 'add_instagram.html', {'form':form})

def add_username(request):
    if request.method=='POST':
        form=Add_intagramForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            find_counts(username)
            
            return redirect('home')
    else:
        form=Add_intagramForm()
    return render(request, 'add_username.html', {'form':form})



