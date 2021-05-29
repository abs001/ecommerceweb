from django.shortcuts import render
from .models import Products


def index(request):
    product_object = Products.objects.all()
    return render(request, 'ecomweb/index.html', {"product_object": product_object})
