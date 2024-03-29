from django.urls import path,include
from django.contrib import admin
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user',views.UserViewSet)
router.register(r'content',views.ContentViewSet)
router.register(r'content_moderation',views.Content_ModerationViewSet)
router.register(r'payments',views.PaymentsViewSet)
router.register(r'advertisements',views.AdvertisementsViewSet)
router.register(r'subscriptions',views.SubscriptionsViewSet)
router.register(r'content_interaction',views.ContentInteractionViewSet)
router.register(r'search',views.Search_RetrievalViewSet)
router.register(r'source',views.SourceViewSet)


urlpatterns = [
    path('',include(router.urls))
] 