from django.http import JsonResponse
from rest_framework.decorators import api_view

from invoice.helpers import sanitize_form_data
from invoice.models import Invoice
from report.models import Report, FileModel


# Save invoice data
@api_view(['POST'])
def add_report(request, *args, **kwargs):
    data = request.data
    try:
        data = sanitize_form_data(dict(data))
        images = data.pop("images", [])
        bulk_create_data = [
            FileModel(file=x)
            for x in images
        ]
        all_saved_images = FileModel.objects.bulk_create(bulk_create_data)
        report = Report.objects.create(**data)
        report.images.set(all_saved_images)
        report.save()
        return JsonResponse(
            status=200,
            data={
                "status": "success",
                "message": "Report created successfully",
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
def get_reports(request, *args, **kwargs):
    reports = Report.objects.all().values()
    return JsonResponse(
        status=200,
        data={
            "status": "success",
            "message": "Reports retrieved successfully",
            "data": list(reports)
        }
    )


# Get single invoice
@api_view(['GET'])
def get_report(request, *args, **kwargs):
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
def update_report(request, *args, **kwargs):
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


@api_view(['DELETE'])
def delete_report(request, *args, **kwargs):
    report_id = kwargs.get("report_id")
    print(report_id)
    try:
        Report.objects.get(id=report_id).delete()
        return JsonResponse(
            status=200,
            data={
                "status": "success",
                "message": "Report deleted successfully",
            }
        )
    except Report.DoesNotExist:
        return JsonResponse(
            status=400,
            data={
                "status": "failed",
                "message": "Invoice not found",
            }
        )
