from django.contrib import admin
from . import views
from import_export.admin import ImportExportModelAdmin
# Register your models here.


admin.site.register(views.User)
# admin.site.register(views.Category)
admin.site.register(views.FileUpload)
admin.site.register(views.ImageDownload)
admin.site.register(views.Contact)


@admin.register(views.Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass