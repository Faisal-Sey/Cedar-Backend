# Generated by Django 4.2.7 on 2024-07-06 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_invoice_presenter_phone_invoice_presenter_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='scope_header_text',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='client_name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='mobile_phone_one',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='mobile_phone_two',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='prepared_by',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='quote_number',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]