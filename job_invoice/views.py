from django.http import JsonResponse
from rest_framework.decorators import api_view

from invoice.helpers import sanitize_form_data
from invoice.models import Invoice
from job_invoice.models import JobInvoice


# Save job invoice data
@api_view(['POST'])
def add_job_invoice(request, *args, **kwargs):
    data = request.data
    try:
        job_invoice = JobInvoice.objects.create(**data)
        job_invoice.invoice_number = f"INT-{job_invoice.id}"
        job_invoice.save()
        return JsonResponse(
            status=200,
            data={
                "status": "success",
                "message": "Invoice created successfully",
                "data": {
                    "invoice_number": job_invoice.invoice_number
                }
            }
        )
    except BaseException as e:
        print(e)
        return JsonResponse(
            status=400,
            data={
                "status": "failed",
                "message": str(e)
            }
        )


# Get all job invoices
@api_view(['GET'])
def get_job_invoices(request, *args, **kwargs):
    invoices = JobInvoice.objects.all().values()
    return JsonResponse(
        status=200,
        data={
            "status": "success",
            "message": "Invoices retrieved successfully",
            "data": list(invoices)
        }
    )


# Get single job invoice
@api_view(['GET'])
def get_job_invoice(request, *args, **kwargs):
    invoice_id = kwargs.get("invoice_id")
    invoice = JobInvoice.objects.filter(id=invoice_id).values().first()
    if invoice is None:
        invoice = {}

    return JsonResponse(
        status=200,
        data={
            "status": "success",
            "message": "Invoice retrieved successfully",
            "data": invoice
        }
    )


# Update single invoice
@api_view(['PATCH'])
def update_job_invoice(request, *args, **kwargs):
    invoice_id = kwargs.get("invoice_id")
    JobInvoice.objects.filter(id=invoice_id).update(**request.data)

    return JsonResponse(
        status=200,
        data={
            "status": "success",
            "message": "Invoice updated successfully",
        }
    )


@api_view(['DELETE'])
def delete_job_invoice(request, *args, **kwargs):
    invoice_id = kwargs.get("invoice_id")
    try:
        Invoice.objects.get(id=invoice_id).delete()
        return JsonResponse(
            status=200,
            data={
                "status": "success",
                "message": "Invoice deleted successfully",
            }
        )
    except Invoice.DoesNotExist:
        return JsonResponse(
            status=400,
            data={
                "status": "failed",
                "message": "Invoice not found",
            }
        )
