from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from app_catalog.models import Product
from app_catalog.forms import ProductForm

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


class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('Index')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('Index')
    template_name = 'catalog/product_delete_confirmation.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'catalog/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('Index')
