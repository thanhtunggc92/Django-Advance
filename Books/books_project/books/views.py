from django.shortcuts import render
from .models import Books,Review
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def BookView(request):
    form = Books.objects.all()
  
    context={'form':form}
    return render(request,'books/book_list.html',context)
@login_required()
def BookDetail(request,pk):
    review=Review.objects.all()
    book_id=Books.objects.get(id=pk)
    book=Books.objects.all()
  

    context={'book_id':book_id,'review':review,'book':book}
    return render(request,'books/book_detail.html',context)