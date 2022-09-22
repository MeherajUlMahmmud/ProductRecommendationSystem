from datetime import datetime, timedelta
from random import randrange

from django.contrib.auth import models as auth_models
from django.db import models
from django.utils import timezone


class MyUserManager(auth_models.UserManager):
    def create_customer(
            self,
            name,
            email,
            password,
            address=None,  # Optional
            is_active=True,
            is_customer=True,
    ):
        # generate otp
        otp = randrange(100000, 999999)

        user = self.model(
            name=name,
            email=email,
            address=address,
            otp=otp,
            otp_expire=datetime.now(tz=timezone.utc) + timedelta(minutes=5),
            is_active=is_active,
            is_customer=is_customer,
            is_verified=True  # As otp verification is not implemented
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_vendor(
            self,
            name,
            email,
            password,
            address=None,  # Optional
            is_active=True,
            is_vendor=True,
    ):
        # generate otp
        otp = randrange(100000, 999999)

        user = self.model(
            name=name,
            email=email,
            address=address,
            otp=otp,
            otp_expire=datetime.now(tz=timezone.utc) + timedelta(minutes=5),
            is_active=is_active,
            is_vendor=is_vendor,
            is_verified=True  # As otp verification is not implemented
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_admin(self, name, email, password, is_active=True, is_admin=True):
        user = self.model(
            name=name,
            email=email,
            is_active=is_active,
            is_admin=is_admin,
            is_verified=True,  # As otp verification is not implemented
            is_staff=is_admin,
            is_superuser=is_admin,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class UserModel(auth_models.AbstractUser):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="user_images", null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_expire = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = None
    first_name = None
    last_name = None

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
