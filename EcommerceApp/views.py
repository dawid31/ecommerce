from django.shortcuts import render

# Create your views here.
def store(request):
    context = {}
    return render (request, 'EcommerceApp/store.html')


def cart(request):
    context = {}
    return render (request, 'EcommerceApp/cart.html')


def checkout(request):
    context = {}
    return render (request, 'EcommerceApp/checkout.html')


def login(request):
    context = {}
    return render (request, 'EcommerceApp/login.html')


def register(request):
    context = {}
    return render (request, 'EcommerceApp/register.html')