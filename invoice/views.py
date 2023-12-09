from django.http import JsonResponse
from rest_framework.decorators import api_view

from invoice.helpers import sanitize_form_data
from invoice.models import Invoice


# Save invoice data
@api_view(['POST'])
def add_invoice(request, *args, **kwargs):
    data = request.data
    try:
        data = sanitize_form_data(dict(data))
        invoice = Invoice.objects.create(**data)
        invoice.quote_number = f"{data.get('invoice_type')}-{invoice.id}-{str(data.get('invoice_date'))[-2:]}"
        invoice.save()
        return JsonResponse(
            status=200,
            data={
                "status": "success",
                "message": "Invoice created successfully",
                "data": {
                    "quote_number": invoice.quote_number
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


# Get all invoices
@api_view(['GET'])
def get_invoices(request, *args, **kwargs):
    invoices = Invoice.objects.all().values()
    return JsonResponse(
        status=200,
        data={
            "status": "success",
            "message": "Invoices retrieved successfully",
            "data": list(invoices)
        }
    )


# Get single invoice
@api_view(['GET'])
def get_invoice(request, *args, **kwargs):
    invoice_id = kwargs.get("invoice_id")
    invoice = Invoice.objects.filter(id=invoice_id).values().first()
    if invoice is None:
        invoice = {}

    return JsonResponse(
        status=200,
        data={
            "status": "success",
            "message": "Invoices retrieved successfully",
            "data": invoice
        }
    )


# Update single invoice
@api_view(['PATCH'])
def update_invoice(request, *args, **kwargs):
    invoice_id = kwargs.get("invoice_id")
    data = sanitize_form_data(dict(request.data))
    signature = data.pop("signature", None)
    Invoice.objects.filter(id=invoice_id).update(**data)
    invoice = Invoice.objects.get(id=invoice_id)
    invoice.signature = signature
    invoice.save()

    return JsonResponse(
        status=200,
        data={
            "status": "success",
            "message": "Invoices retrieved successfully",
        }
    )