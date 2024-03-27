from django.contrib import admin
from . import views
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