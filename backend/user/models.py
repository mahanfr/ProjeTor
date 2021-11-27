from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from company.models import Company, Position


# This is a class for managing our custom user authentication
class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, user_name, phone_number, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(_('SuperUser must be assigned to is_staff'))

        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('SuperUser must be assigned to is_superuser'))

        return self.create_user(email, user_name, phone_number, password, **other_fields)

    def create_user(self, email, user_name, phone_number, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        # TODO: Check for valid phone number
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user


# This class created to add and replace some features
# of default django user model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=80, unique=True)
    user_name = models.CharField(max_length=80, unique=True)
    first_name = models.CharField(max_length=80, blank=True, null=True)
    last_name = models.CharField(max_length=80, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    verified_at = models.DateTimeField(blank=True, null=True)
    premiered_at = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'user_name']


class Profile(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    position = models.ForeignKey(
        'company.Position', on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(
        'company.Company', on_delete=models.SET_NULL, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_picture/', blank=True, null=True, default='profile_picture/default.png')

    def __str__(self):
        return self.user.user_name
