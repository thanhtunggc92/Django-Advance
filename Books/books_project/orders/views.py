from django.shortcuts import render

# Create your views here.
def OrderPageView(request):
    context={}

    return render(request,'order/purchase.html',context)