# Generated by Django 4.2.7 on 2024-07-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0014_report_inspector_signature_report_reviewer_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_title',
            field=models.TextField(blank=True),
        ),
    ]
