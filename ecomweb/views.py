from django.shortcuts import render
from .models import Products
from django.core.paginator import Paginator


def index(request):
    product_object = Products.objects.all()

    # Search
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_object = product_object.filter(title__icontains=item_name)

    # Paginator
    paginator = Paginator(product_object, 8)
    page_data = request.GET.get('page')
    product_object = paginator.get_page(page_data)

    return render(request, 'ecomweb/index.html', {"product_object": product_object})

