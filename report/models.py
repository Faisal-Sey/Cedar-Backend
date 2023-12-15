from django.db import models


class AssetDetail(models.Model):
    type = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    model = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    material = models.CharField(max_length=255)


class BodyDetail(models.Model):
    body_condition = models.CharField(max_length=255)
    bore_condition = models.CharField(max_length=255)
    bore_debris_free = models.CharField(max_length=255)
    shoulder_to_shoulder = models.CharField(max_length=255)
    float_type = models.CharField(max_length=255, blank=True)
    i_d = models.CharField(max_length=255, blank=True)


class BladeDetail(models.Model):
    blade_condition = models.CharField(max_length=255)
    blade_length = models.CharField(max_length=255)
    blade_width = models.CharField(max_length=255)
    blade_od_center = models.CharField(max_length=255)
    actual_od_fn = models.CharField(max_length=255, blank=True)
    actual_od_center = models.CharField(max_length=255, blank=True)
    actual_od_tn = models.CharField(max_length=255, blank=True)
    dressing_type = models.CharField(max_length=255, blank=True)


class StatusHandler(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    qualification = models.CharField(max_length=255)


class Consumables(models.Model):
    type = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    batch_number = models.CharField(max_length=255)
    expiry_date = models.CharField(max_length=255)
    services = models.CharField(max_length=255)


class Personnel(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    services = models.CharField(max_length=255)


class ReportKeys(models.Model):
    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=255)


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
    revision = models.CharField(max_length=255)
    examination_date = models.CharField(max_length=255)
    next_examination_date = models.DateField(blank=True, null=True)
    examination_area = models.CharField(max_length=255)
    services = models.CharField(max_length=255)
    standards = models.CharField(max_length=255)
    local_procedure_number = models.CharField(max_length=255)
    drawing_number = models.CharField(max_length=255, blank=True)
    test_restrictions = models.CharField(max_length=255)
    surface_condition = models.CharField(max_length=255)
    asset_details = models.ManyToManyField(
        AssetDetail,
        related_name="asset_details"
    )
    dimension_one_name = models.CharField(max_length=10)
    dimension_two_name = models.CharField(max_length=10)
    dimension_one = models.JSONField()
    dimension_two = models.JSONField()
    body = models.ForeignKey(BodyDetail, on_delete=models.CASCADE, null=True)
    blade = models.ForeignKey(BladeDetail, on_delete=models.CASCADE, null=True)
    visual = models.TextField()
    report_type_data = models.JSONField()
    report_status = models.CharField(max_length=50)
    issuer = models.ForeignKey(
        StatusHandler,
        on_delete=models.CASCADE,
        related_name='issuer_details'
    )
    quality_controller = models.ForeignKey(
        StatusHandler,
        on_delete=models.CASCADE,
        related_name='quality_details'
    )
    acceptor = models.ForeignKey(
        StatusHandler,
        on_delete=models.CASCADE,
        related_name='acceptor_details',
        null=True
    )
    consumables = models.ManyToManyField(
        Consumables,
        related_name="consumables"
    )
    comments = models.TextField()
    keys = models.ManyToManyField(
        ReportKeys,
        related_name="report_keys"
    )
    images = models.ImageField(upload_to="reports/")
    created_on = models.DateTimeField(auto_now=True)
    objects = models.Manager()
