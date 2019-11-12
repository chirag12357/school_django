from django.shortcuts import render
import csv
# Create your views here.
def compfunc(request):
    if request.method == 'POST':
        dict1 = request.POST.dict()
        print(dict1)
        with open('orders.csv','a') as csvfile:
            wrt = csv.writer(csvfile)
            wrt.writerow([dict1['name'],dict1['email'],dict1['phno'],dict1['appliance']])
    return render(request,"complaint.html")
