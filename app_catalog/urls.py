from django.urls import path

from app_catalog.views import index_view, contacts_view


urlpatterns = [
    path('', index_view, name='Index'),
    path('contacts/', contacts_view, name='contacts'),
]
