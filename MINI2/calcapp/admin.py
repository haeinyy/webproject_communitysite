from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from calcapp.models import Attendences, Blog

class AH_Admin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Attendences, AH_Admin)
admin.site.register(Blog)
