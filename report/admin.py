from django.contrib import admin

from report.models import Report, FileModel

# Register your models here.
admin.site.register(Report)
admin.site.register(FileModel)