from django.contrib import admin
from . import views
from import_export.admin import ImportExportModelAdmin
# Register your models here.


admin.site.register(views.User)
admin.site.register(views.Content)
admin.site.register(views.Content_Moderation)
admin.site.register(views.Payments)
admin.site.register(views.Advertisements)
admin.site.register(views.Subscriptions)
admin.site.register(views.ContentInteraction)
admin.site.register(views.Search_Retrieval)
admin.site.register(views.Source)
# admin.site.register(views.Category)
admin.site.register(views.FileUpload)
admin.site.register(views.ImageDownload)
admin.site.register(views.Contact)


@admin.register(views.Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass