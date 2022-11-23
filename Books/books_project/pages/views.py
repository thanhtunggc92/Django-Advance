from django.shortcuts import render

# Create your views here.


def HomePage(request):
    context={}
    return render(request,'home.html',context)

def AboutView(request):
    context={}
    return render (request,'about.html',context)