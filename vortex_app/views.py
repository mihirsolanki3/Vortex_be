import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import render
from vortex_app.models import *
from vortex_app.serializer import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from django.core.files.base import ContentFile
from rest_framework.pagination import PageNumberPagination


class FileUploadPagination(PageNumberPagination):
    page_size = 10  # Adjust the page size as needed
    page_size_query_param = 'page_size'
    max_page_size = 100

# from django.contrib.auth import get_user_model

# User = get_user_model()


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {
            'user': str(request.user),
            'email': str(request.user.email),
            'first_name': str(request.user.first_name),
            'last_name': str(request.user.last_name),
        }
        return Response(content)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer


class FileUploadViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    queryset = FileUpload.objects.all().order_by('?')
    serializer_class = FileUpload_Serializer
    search_fields = ['category__category_name']
    filterset_fields = ['category']
    pagination_class = FileUploadPagination


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = Content_Serializer


class Content_ModerationViewSet(viewsets.ModelViewSet):
    queryset = Content_Moderation.objects.all()
    serializer_class = Content_Moderation_Serializer


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = Payments_Serializer


class AdvertisementsViewSet(viewsets.ModelViewSet):
    queryset = Advertisements.objects.all()
    serializer_class = Advertisements_Serializer


class SubscriptionsViewSet(viewsets.ModelViewSet):
    queryset = Subscriptions.objects.all()
    serializer_class = Subscriptions_Serializer


class ContentInteractionViewSet(viewsets.ModelViewSet):
    queryset = ContentInteraction.objects.all()
    serializer_class = ContentInteraction_Serializer


class Search_RetrievalViewSet(viewsets.ModelViewSet):
    queryset = Search_Retrieval.objects.all()
    serializer_class = Search_Retrieval_Serializer


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = Source_Serializer


def download_photo_from_unsplash(request):
    categories = Category.objects.all()
    for category in categories:
        for page in range(1, 100):
            response = requests.get(
                "https://api.unsplash.com/search/photos/", params={"client_id": "zF8Ku92rcNtoldkP2sKie1-Vs8h9B6OK9LIqTKoDrdM", "query": category.category_name, "page": page}
            )
            if response.status_code == 200:
                photo_data = response.json()['results']
                for picture in photo_data:
                    photo_url = picture.get("urls").get("full")
                    photo_response = requests.get(photo_url)
                    if photo_response.status_code == 200:
                        photo_content = photo_response.content

                        photo = FileUpload()
                        photo.category = category
                        photo.image.save(
                            f'{picture.get("slug")}.jpg', ContentFile(photo_content))
                        photo.save()
        return JsonResponse({"status": "success", "message": "Downloaded"})
