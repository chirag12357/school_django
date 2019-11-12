from django.shortcuts import render

# Create your views here.
def welcfunc(request):
    return render(request,"welcome.html")
