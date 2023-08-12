from django.urls import path
from django.views.decorators.cache import cache_page

from app_catalog.views import IndexView, ContactsView, ProductView, ProductCreateView, ProductDeleteView, ProductUpdateView



urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductView.as_view()), name='product'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
]
