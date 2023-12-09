from django.db import models


class Invoice(models.Model):
    invoice_name = models.CharField(max_length=500)
    prepared_by = models.CharField(max_length=255)
    client_name = models.CharField(max_length=500)
    invoice_date = models.DateField()
    requirements = models.TextField()
    scope = models.JSONField()
    costs = models.JSONField()
    responsibilities = models.JSONField()
    resources = models.JSONField()
    terms = models.JSONField()
    quote_number = models.CharField(max_length=255)
    invoice_type = models.CharField(max_length=255)
    last_words = models.TextField()
    mobile_phone_one = models.CharField(max_length=20)
    mobile_phone_two = models.CharField(max_length=20)
    signature = models.ImageField(null=True)
    email = models.EmailField()
    presenter_phone = models.CharField(max_length=20, blank=True)
    presenter_role = models.CharField(max_length=255, blank=True)

    objects = models.Manager()
