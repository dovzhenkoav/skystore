from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = "redirect_to"

    model = Product
    template_name = 'catalog/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('Index')

    def form_valid(self, form):
        if form.is_valid():
            new_form = form.save()
            new_form.author = self.request.user
            new_form.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = "redirect_to"

    model = Product
    success_url = reverse_lazy('Index')
    template_name = 'catalog/product_delete_confirmation.html'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = "redirect_to"

    model = Product
    template_name = 'catalog/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('Index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Модель1 - модель2 - форма из forms.py - сколько раз надо повторить её на странице
        ProductFormset = inlineformset_factory(Product, Version, form=ProductForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
