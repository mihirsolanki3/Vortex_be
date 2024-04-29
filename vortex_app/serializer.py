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


class Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
