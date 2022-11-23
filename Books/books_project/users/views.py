


from django.shortcuts import render,redirect
from .models import Users
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomRegisterForm
# Create your views here.
def Login(request):
    form=AuthenticationForm()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user) 
            return redirect('home')
    context={'form':form}
    return render(request,'register/login.html',context)
def Logout(request):
    logout(request)
    messages.info(request,'You are log out.!!')
    return redirect('home')
def SignUpForm(request):
    form =CustomRegisterForm()
    if request.method=='POST':
        form=CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context={'form':form}
    return render(request,'register/signup.html',context)
