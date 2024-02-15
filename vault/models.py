from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils.text import slugify


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(email=email, **kwargs)

        user.set_password(password)

        # Generate a unique username based on first and last names
        base_username = slugify(f"{user.first_name} {user.last_name}")
        user.username = base_username
        i = 1
        while self.model.objects.filter(username=user.username).exists():
            user.username = f"{base_username}-{i}"
            i += 1

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password=password, **kwargs)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.username
