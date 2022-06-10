"""Models for users"""
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import MyUserManager

LOCATIONS_CHOISES = (
    ('mexico','MEXICO'),
    ('colombia', 'COLOMBIA'),
    ('peru','PERU'),
    ('chile','CHILE'),
    ('brazil','BRAZIL'),
    )
USER_TYPE_CHOICES = (
    ('mentor', 'Mentor'),
    ('member', 'Member'),
    )

class User(AbstractBaseUser, PermissionsMixin):
    """User model table"""
    email = models.EmailField(
        verbose_name='email', 
        max_length=60, 
        unique=True
        )
    username = models.CharField(
        max_length=30, 
        unique=True
        )
    date_joined = models.DateField(
        verbose_name='date joined', 
        auto_now_add=True
        )
    last_login = models.DateField(
        verbose_name='last login', 
        auto_now=True
        )
    is_admin = models.BooleanField(
        default=False
        )
    is_active = models.BooleanField(
        default=True
        )
    is_staff = models.BooleanField(
        default=False
        )
    is_superuser = models.BooleanField(
        default=False
        )
    rating = models.FloatField(
        default=0, 
        blank=True, 
        null=True
        )
    reviews_count = models.IntegerField(
        default=0
        )
    first_name = models.CharField(
        verbose_name=_('first_name'), 
        max_length=30
        )
    last_name = models.CharField(
        verbose_name=_('last_name'), 
        max_length=30
        )
    location = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        choices=LOCATIONS_CHOISES,
        verbose_name=_("The Place where you live like"),
        help_text=_("format: required, max-100"),
    )
    employer = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Your employer"),
        help_text=_("format: required, max-100"),
    )
    user_type = models.CharField(
        max_length=40,
        null=False,
        unique=False,
        blank=False,
        choices=USER_TYPE_CHOICES,
        verbose_name=_("User type"),
        help_text=_("format: required, max-40"),
        )
    title = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Your title"),
        help_text=_("format: required, max-100"),
    )

    USERNAME_FIELD = 'email' 
#this field means that when you try to sign in the username field will be the email 
#change it to whatever you want django to see as the username when authenticating the user
    REQUIRED_FIELDS = ['user_type']

    objects = MyUserManager()