from django.shortcuts import render
import csv

# Create your views here.
def myorder(request):
    if request.method == 'POST':
        dict1 = request.POST.dict()
        print(dict1)
        with open('orders.csv','a') as csvfile:
            wrt = csv.writer(csvfile)
            wrt.writerow([dict1['name'],dict1['add'],dict1['num'],dict1['qty']])
    return render(request,'order.html')
