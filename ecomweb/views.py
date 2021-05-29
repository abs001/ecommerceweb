from django.shortcuts import render
from .models import Products


def index(request):
    product_object = Products.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_object = product_object.filter(title__icontains=item_name)
    return render(request, 'ecomweb/index.html', {"product_object": product_object})
