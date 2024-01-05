from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('add-job-invoice/', views.add_job_invoice, name="add_job_invoice"),
    path('get-job-invoices/', views.get_job_invoices, name="get_job_invoices"),
    path('get-job-invoice/<int:invoice_id>/', views.get_job_invoice, name="get_job_invoice"),
    path('update-job-invoice/<int:invoice_id>/', views.update_job_invoice, name="update_job_invoice"),
    # path('delete-invoice/<int:invoice_id>/', views.delete_invoice, name="delete_invoice"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
