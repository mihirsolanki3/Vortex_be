from django.urls import path, include
from django.contrib import admin
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'fileupload', views.FileUploadViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('profile/', views.ProfileView.as_view()),
    path('contact/', views.ConatctView.as_view()),
    path('download-image/<id>/', views.DownloadImageView.as_view()),
    path('photo/', views.download_photo_from_unsplash),
    path('payment/', views.payment),
    path('response/', views.response),
    path('getCollection/', views.getCollection),
]
