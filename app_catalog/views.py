from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView

from app_catalog.models import Product

# Create your views here.


class IndexView(ListView):
    model = Product
    template_name = 'catalog/index.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} {phone} {message}')
        return render(request, 'catalog/contacts.html')


class ProductView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = "product"
