from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager

# Abstructuser


class User(AbstractUser):
    user_bio = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(max_length=100, null=True, blank=True, default="free", choices=(
        ("free", "Free"), ("professional", "Professional"), ("enterprise", "Enterprise")))
    objects = UserManager()


# create Models.


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name


class FileUpload(models.Model):
    image = models.FileField(upload_to="uploads/")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.PROTECT)


# creating Content model.
class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    source_name = models.CharField(max_length=50)
    description = models.TextField()
    upload_date = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=50)


class Content_Moderation(models.Model):
    moderation_id = models.AutoField(primary_key=True)
    moderator_id = models.ForeignKey(
        User, default=None, on_delete=models.PROTECT)
    content_id = models.ForeignKey(
        Content, default=None, on_delete=models.PROTECT)
    moderation_status = models.TextField()
    moderation_date = models.DateTimeField(auto_now_add=True)


class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    payment_amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=100)


class Advertisements(models.Model):
    ad_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    ad_title = models.CharField(max_length=50)
    ad_description = models.TextField()
    ad_imageurl = models.CharField(max_length=100)
    ad_linkurl = models.CharField(max_length=100)
    ad_startdate = models.DateTimeField()
    ad_enddate = models.DateTimeField()
    adstatus_active = models.BooleanField(default=False)
    adstatus_inactive = models.BooleanField(default=False)
    payment_id = models.ForeignKey(
        Payments, default=None, on_delete=models.PROTECT)


class Subscriptions(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    subscription_type = models.CharField(max_length=50)
    subscription_status = models.CharField(max_length=100)
    subscription_startdate = models.DateTimeField()
    subscription_enddate = models.DateTimeField()
    payment_amount = models.FloatField()
    payment_date = models.DateTimeField()
    payment_id = models.ForeignKey(
        Payments, default=None, on_delete=models.PROTECT)


class ContentInteraction(models.Model):
    interaction_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    interaction_type = models.CharField(max_length=50)
    content_id = models.ForeignKey(
        Content, default=None, on_delete=models.PROTECT)


class Search_Retrieval(models.Model):
    searchengine = models.CharField(max_length=50)
    content_api = models.CharField(max_length=100)


class Source(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=50)
    api_endpoint = models.CharField(max_length=100)
    apikey = models.CharField(max_length=50)


class ImageDownload(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    count = models.IntegerField(default=0)
    date = models.DateField()
