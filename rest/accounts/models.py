from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
import uuid


class UserManager(BaseUserManager):
    """
    email = models.EmailField(
        verbose_name='E-Mail Adresse',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=100, null=False, default='', verbose_name='Vorname')
    last_name = models.CharField(max_length=100, null=False, default='', verbose_name='Nachname')
    active = models.BooleanField(default=True, verbose_name='Ist Aktiviert?')
    staff = models.BooleanField(default=False, verbose_name='Ist Administrator?')
    admin = models.BooleanField(default=False, verbose_name='Ist Super-Administrator')
    """
    def create_user(self, email, first_name, last_name, active=True, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            active=active,
            staff=False,
            admin=False
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4)

    email = models.EmailField(
        verbose_name='E-Mail Adresse',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=100, null=False, default='', verbose_name='Vorname')
    last_name = models.CharField(max_length=100, null=False, default='', verbose_name='Nachname')
    active = models.BooleanField(default=True, verbose_name='Ist Aktiviert?')
    staff = models.BooleanField(default=False, verbose_name='Ist Administrator?')
    admin = models.BooleanField(default=False, verbose_name='Ist Super-Administrator')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
       return str(self.first_name) + " " + str(self.last_name) + " (" + str(self.email) + ")"

    def has_perm(self, perm, obj=None):
        if self.admin:
            return True
        else:
            return super().has_perm(perm=perm, obj=obj)

    def has_module_perms(self, app_label):
        if self.admin:
            return True
        else:
            return super().has_module_perms(app_label=app_label)

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    class Meta:
        verbose_name = 'Nutzer'
        verbose_name_plural = 'Benutzer'