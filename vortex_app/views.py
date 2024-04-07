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
#from django.contrib.auth import get_user_model

#User = get_user_model()
    
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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    queryset = FileUpload.objects.all()
    serializer_class = FileUpload_Serializer
    search_fields = ['category__category_name']
    filterset_fields = ['category']
    
class ContentViewSet(viewsets.ModelViewSet):
    queryset=Content.objects.all()
    serializer_class=Content_Serializer

class Content_ModerationViewSet(viewsets.ModelViewSet):
    queryset=Content_Moderation.objects.all()
    serializer_class=Content_Moderation_Serializer   

class PaymentsViewSet(viewsets.ModelViewSet):
    queryset=Payments.objects.all()
    serializer_class=Payments_Serializer   

class AdvertisementsViewSet(viewsets.ModelViewSet):
    queryset=Advertisements.objects.all()
    serializer_class=Advertisements_Serializer    

class SubscriptionsViewSet(viewsets.ModelViewSet):
    queryset=Subscriptions.objects.all()
    serializer_class=Subscriptions_Serializer      

class ContentInteractionViewSet(viewsets.ModelViewSet):
    queryset=ContentInteraction.objects.all()
    serializer_class=ContentInteraction_Serializer 

class Search_RetrievalViewSet(viewsets.ModelViewSet):
    queryset=Search_Retrieval.objects.all()
    serializer_class=Search_Retrieval_Serializer        

class SourceViewSet(viewsets.ModelViewSet):
    queryset=Source.objects.all()
    serializer_class=Source_Serializer          
