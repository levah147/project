from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'dasborad/index.html')

def staff(request):
    return render(request,'dasborad/staff.html')

def order(request):
    return render(request,'dasborad/order.html')

def product(request):
    return render(request,'dasborad/product.html')