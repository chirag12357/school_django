from django.shortcuts import render

# Create your views here.
def mylist(request):
    return render(request,'list.html')
