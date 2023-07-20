from django.urls import path

from app_catalog.views import IndexView, ContactsView, ProductView


urlpatterns = [
    path('', IndexView.as_view(), name='Index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductView.as_view(), name='product'),
]
