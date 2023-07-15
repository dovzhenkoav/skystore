from django.shortcuts import render

from app_catalog.models import Product

# Create your views here.


def index_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalog/index.html', context=context)


def contacts_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone} {message}')
    return render(request, 'catalog/contacts.html')



def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context=context)




