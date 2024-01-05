from django.db import models


class JobInvoice(models.Model):
    invoice_number = models.CharField(max_length=100, blank=True)
    receiver = models.CharField(max_length=255)
    currency = models.CharField(max_length=10)
    receiver_address = models.CharField(max_length=500)
    invoice_date = models.DateField()
    due_date = models.DateField()
    invoice_data = models.JSONField()
    subtotal = models.FloatField(default=0.0)
    nhl = models.FloatField(default=0.0)
    getfl = models.FloatField(default=0.0)
    covid = models.FloatField(default=0.0)
    total_before_tax = models.FloatField(default=0.0)
    vat = models.FloatField(default=0.0)
    total_amount = models.FloatField(default=0.0)

    objects = models.Manager()