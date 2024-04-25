from rest_framework import serializers
from .models import *

# create serializers


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        user = User.objects.create(**validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class FileUpload_Serializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = FileUpload
        fields = "__all__"

    def get_category_name(self, obj):
        return obj.category.category_name

    def create(self, validated_data):
        # Check if user is logged in
        if self.context['request'].user.is_authenticated:
            # If logged in, associate the current user with the uploaded file
            validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class Content_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class Content_Moderation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Content_Moderation
        fields = "__all__"


class Payments_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class Advertisements_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisements
        fields = "__all__"


class Subscriptions_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = "__all__"


class ContentInteraction_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ContentInteraction
        fields = "__all__"


class Search_Retrieval_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Search_Retrieval
        fields = "__all__"


class Source_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"


class Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
