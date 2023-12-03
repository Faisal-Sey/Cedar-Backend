from django.http import JsonResponse
from rest_framework.decorators import api_view

from invoice.models import Invoice


@api_view(['POST'])
def add_invoice(request, *args, **kwargs):
    data = request.data.get("invoiceData")
    try:
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