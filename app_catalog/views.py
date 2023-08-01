from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from app_catalog.models import Product, Version
from app_catalog.forms import ProductForm

# Create your views here.


class IndexView(ListView):
    model = Product
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_versions = Version.objects.filter(is_active=True)
        for product in context['object_list']:
            version = active_versions.filter(product=product)
            if version:
                product.version = {
                    'name': version[0].name,
                    'number': version[0].number,
                }
                print(product.version)
        return context


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
