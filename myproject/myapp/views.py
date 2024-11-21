from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def faq(request):
    return render(request,"faq.html")
def index(request):
    return render(request,"index.html")
def product_detail(request):
    return render(request,"product-detail.html"),
def products(request):
    return render(request,"products.html")
def sign_in(request):
    return render(request,"sign-in.html")
def sign_up(request):
    return render(request,"sign-up.html")

