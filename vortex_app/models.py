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


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.category_name)


class FileUpload(models.Model):
    image = models.FileField(upload_to="uploads/")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return str(self.image)


class ImageDownload(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    count = models.IntegerField(default=0)
    date = models.DateField()
    
    def __str__(self) -> str:
        return str(self.user)


class Contact(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    company = models.CharField(max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.first_name)