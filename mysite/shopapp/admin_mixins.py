"""
This Python code snippet defines a Django Mixin called ExportAsCSVMixin that provides functionality
to export model data as a CSV file through a Django view.
This mixin can be integrated with Django admin or any other Django view to enable CSV exports.
Below is a detailed breakdown of the components and functionality provided by the ExportAsCSVMixin class.
"""

from django.db.models import QuerySet
from django.db.models.options import Options
from django.http import HttpRequest, HttpResponse


class ExportAsCSVMixin:
    def export_csv(self, request: HttpRequest, queryset: QuerySet):
        meta: Options = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}-export.csv'

        csv_writer = csv.writer(response)

        csv_writer.writerow(field_names)

        for obj in queryset:
            csv_writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_csv.short_description = 'Export as CSV'