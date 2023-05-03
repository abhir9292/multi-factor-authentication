from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import MyAccountManager
import hashlib

class Account(AbstractBaseUser):
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
        (4, '...')
    )
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    other_names = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, null=True, blank=True)
    gender = models.IntegerField(default=4)
    phone = models.CharField(max_length=15, null=True)
    details = models.TextField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_subscribed = models.BooleanField(default=False)
    subscribed_on = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def get_short_name(self):
        username = self.username
        if not username:
            username = self.first_name
        if not username:
            username = self.last_name
        if not username:
            username = self.email
        if not username:
            username = 'Guest'
        return username


    @property
    def get_full_name(self):
        full_name = ''
        if self.first_name:
            full_name += f"{self.first_name.title()} "
        if self.other_names:
            for name in self.other_names.split():
                full_name += f"{name[0].upper()}."
            full_name += ' '
        if self.last_name:
            full_name += f"{self.last_name.title()}"
        full_name = full_name.strip()
        if not full_name:
            return self.get_short_name
        return full_name

    @property
    def get_avatar(self):
        email = self.email
        email_hash = hashlib.md5(email.encode()).hexdigest()
        root_url = 'https://www.gravatar.com/avatar/'
        default = 'patlys.co.ke/static/img/ke.png'
        avatar = f"{root_url}{email_hash}?d={default}"
        return avatar