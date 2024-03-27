from rest_framework import serializers
from .models import *

#create serializers
class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields="__all__"
        
class Content_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Content
        fields="__all__"

class Content_Moderation_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Content_Moderation
        fields="__all__"        

class Payments_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Payments
        fields="__all__"      

class Advertisements_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Advertisements
        fields="__all__"         

class Subscriptions_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Subscriptions
        fields="__all__"    

class ContentInteraction_Serializer(serializers.ModelSerializer):
    class Meta:
        model= ContentInteraction
        fields="__all__"   

class Search_Retrieval_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Search_Retrieval
        fields="__all__"   

class Source_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Source
        fields="__all__"     
                



