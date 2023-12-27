from django.db import models


class FileModel(models.Model):
    file = models.ImageField(upload_to='reports/')
    objects = models.Manager()


class Report(models.Model):
    report_type = models.CharField(max_length=50)
    client_name = models.CharField(max_length=500)
    client_address = models.TextField()
    client_city = models.CharField(max_length=255)
    client_country = models.CharField(max_length=200)
    examination_location = models.TextField()
    contract = models.CharField(max_length=200, blank=True, default="-")
    work_order = models.CharField(max_length=255)
    purchase_order = models.CharField(max_length=255, blank=True, default="-")
    client_job_reference = models.CharField(max_length=255)
    rig = models.CharField(max_length=255, blank=True, default="-")
    report_number = models.CharField(max_length=255)
    examination_date = models.CharField(max_length=255)
    next_examination_date = models.DateField(blank=True, null=True)
    examination_area = models.CharField(max_length=255)
    services = models.CharField(max_length=255)
    standards = models.CharField(max_length=255)
    local_procedure_number = models.CharField(max_length=255)
    drawing_number = models.CharField(max_length=255, blank=True)
    test_restrictions = models.CharField(max_length=255)
    surface_condition = models.CharField(max_length=255)
    asset_details = models.JSONField()
    dimension_one_name = models.CharField(max_length=10)
    dimension_two_name = models.CharField(max_length=10)
    dimension_one = models.JSONField()
    dimension_two = models.JSONField()
    body = models.JSONField()
    blade = models.JSONField()
    visual = models.TextField()
    report_type_data = models.JSONField()
    report_status = models.CharField(max_length=50)
    issuer = models.JSONField()
    quality_controller = models.JSONField()
    consumables = models.JSONField()
    equipments = models.JSONField()
    comments = models.TextField()
    keys = models.JSONField()
    images = models.ManyToManyField(
        FileModel,
        related_name="Report_files"
    )
    created_on = models.DateTimeField(auto_now=True)
    objects = models.Manager()
