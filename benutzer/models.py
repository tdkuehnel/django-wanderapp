from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.utils import timezone
from simple_history import register
from PIL import Image

import datetime

# Create your models here.


class BenutzerManager(UserManager):

    def get_by_natural_key(self, username):
        return self.get(username=username)

class Benutzer(AbstractBaseUser, PermissionsMixin):
    id               = models.AutoField('ID', primary_key=True, db_column='bnz_id')
    username         = models.CharField('Benutzername', max_length=64, db_column='bnz_bname', blank=True, null=True, unique=True)
    email            = models.EmailField('E-Post-Adresse',
                                        max_length=128, blank=True, default='', null=False, db_column='bnz_email')
    date_joined      = models.DateTimeField(default=timezone.now)
    is_staff         = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=True)
    is_superuser     = models.BooleanField(
        default=False,
        help_text='Designates that this user has all permissions without explicitly assigning them.',
        verbose_name='superuser status'
    )
    groups = models.ManyToManyField(
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='user_set',
        related_query_name='user',
        to='auth.Group',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='user_set',
        related_query_name='user',
        to='auth.Permission',
        verbose_name='user permissions'
    )

    avatar = models.ImageField(
        default='avatar.jpg', # default avatar
        upload_to='profile_avatars' # dir to store the image
    )

    objects = BenutzerManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return f'Profil: {self.username}.'
        #(self.username)

    def get_name(self):
        return self.username
    
    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)

    class Meta:
        app_label = 'benutzer'
        db_table = "benutzer"
        verbose_name = "Benutzer"
        verbose_name_plural = "Benutzer"
        permissions = [
            ("berechtigung", "Berechtigung"),
        ]

register(Benutzer)
