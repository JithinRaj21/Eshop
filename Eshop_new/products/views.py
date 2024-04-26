from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Products


# Create your views here.
def home(request):
    product = Products.objects.all()
    return render(request, 'home.html', {'product': product})


def product_detail(request, pk):
    products = Products.objects.get(pk=pk)
    return render(request, 'detail_product.html', {'products': products})


def list_products(request):
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)

    product_list = Products.objects.order_by('-priority')
    product_paginator = Paginator(product_list, 2)
    product_list = product_paginator.get_page(page)
    context = {'products': product_list}
    return render(request, 'products.html', context)