from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('add-invoice/', views.add_invoice, name="add_invoice"),
    path('get-invoices/', views.get_invoices, name="get_invoices"),
    path('get-invoice/<int:invoice_id>/', views.get_invoice, name="get_invoice"),
    path('update-invoice/<int:invoice_id>/', views.update_invoice, name="update_invoice"),
    path('delete-invoice/<int:invoice_id>/', views.delete_invoice, name="delete_invoice"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
