from django.urls import path
from . import views

urlpatterns = [
    path('add-report/', views.add_report, name="add_report"),
    path('get-reports/', views.get_reports, name="get_reports"),
    path('get-report/<int:report_id>/', views.get_report, name="get_report"),
    path('update-report/<int:report_id>/', views.update_report, name="update_report"),
    path('delete-report/<int:report_id>/', views.delete_report, name="delete_report"),
]
