from django.urls import path
from . import views

urlpatterns = [
    path('add-invoice/', views.add_invoice, name="add_invoice"),
    path('get-invoices/', views.get_invoices, name="get_invoices"),
]