from django.forms import model_to_dict
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
        images = data.pop("images", [])
        file_names = data.pop("file_names", [])
        data = sanitize_form_data(dict(data))
        bulk_create_data = [
            FileModel(file=x, name=file_names[index])
            for index, x in enumerate(images)
        ]
        print(bulk_create_data)
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
    reports = Report.objects.prefetch_related("images").all()
    reports_list = []
    for report in reports:
        report_images = list(report.images.all().values())
        modified_report = model_to_dict(
            report,
            exclude=[
                'drawing_image_one',
                'drawing_image_two',
                'inspector_signature',
                'reviewer_signature'
            ]
        )
        modified_report[
            'drawing_image_one_url'] = report.drawing_image_one.url if report.drawing_image_one else None
        modified_report[
            'drawing_image_two_url'] = report.drawing_image_two.url if report.drawing_image_two else None
        modified_report[
            'inspector_signature_url'] = report.inspector_signature.url if report.inspector_signature else None
        modified_report[
            'reviewer_signature_url'] = report.reviewer_signature.url if report.reviewer_signature else None
        modified_report["images"] = report_images
        reports_list.append(modified_report)

    return JsonResponse(
        status=200,
        data={
            "status": "success",
            "message": "Reports retrieved successfully",
            "data": reports_list
        }
    )


# Get single invoice
@api_view(['GET'])
def get_report(request, *args, **kwargs):
    report_id = kwargs.get("report_id")
    try:
        report = Report.objects.prefetch_related("images").get(id=report_id)
        report_images = list(report.images.all().values())
        modified_report = model_to_dict(
            report,
            exclude=[
                'drawing_image_one',
                'drawing_image_two',
                'inspector_signature',
                'reviewer_signature'
            ]
        )
        modified_report[
            'drawing_image_one_url'] = report.drawing_image_one.url if report.drawing_image_one else None
        modified_report[
            'drawing_image_two_url'] = report.drawing_image_two.url if report.drawing_image_two else None
        modified_report["images"] = report_images
        modified_report[
            'inspector_signature_url'] = report.inspector_signature.url if report.inspector_signature else None
        modified_report[
            'reviewer_signature_url'] = report.reviewer_signature.url if report.reviewer_signature else None

        return JsonResponse(
            status=200,
            data={
                "status": "success",
                "message": "Report retrieved successfully",
                "data": modified_report
            }
        )
    except Report.DoesNotExist:
        return JsonResponse(
            status=400,
            data={
                "status": "error",
                "message": "Report does not exist",
            }
        )


# Update single invoice
@api_view(['PATCH'])
def update_report(request, *args, **kwargs):
    report_id = kwargs.get("report_id")
    data = sanitize_form_data(dict(request.data))
    images = data.pop("images", [])
    file_names = data.pop("file_names", [])
    bulk_create_data = [
        FileModel(file=x, name=file_names[index])
        for index, x in enumerate(images)
    ]
    all_saved_images = FileModel.objects.bulk_create(bulk_create_data)
    Report.objects.filter(id=report_id).update(**data)
    report = Report.objects.get(id=report_id)
    report.images.set(all_saved_images)
    report.save()

    return JsonResponse(
        status=200,
        data={
            "status": "success",
            "message": "Report updated successfully",
        }
    )


@api_view(['DELETE'])
def delete_report(request, *args, **kwargs):
    report_id = kwargs.get("report_id")
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
