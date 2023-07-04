import uuid

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


class AbstractManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            return self.get(public_id=public_id)
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    # def create_user(self, username, email, password=None, **kwargs):
    #     if username is None:
    #         raise TypeError('Users must have a username.')
    #     if email is None:
    #         raise TypeError('Users must have an email.')
    #     if password is None:
    #         raise TypeError('User must have an email.')
    #
    #     user = self.model(
    #         username=username,
    #         email=self.normalize_email(email),
    #         **kwargs,
    #     )
    #     user.set_password(password)
    #     user.save(using=self._db)
    #
    #     return user
    #
    # def create_superuser(self, username, email, password=None, **kwargs):
    #     if password is None:
    #         raise TypeError('Superusers must have a password.')
    #     if email is None:
    #         raise TypeError('Superusers must have an email.')
    #     if username is None:
    #         raise TypeError('Superusers must have an username.')
    #
    #     user = self.create_user(
    #         username,
    #         email,
    #         password,
    #         **kwargs,
    #     )
    #     user.is_superuser = True
    #     user.is_staff = True
    #     user.save(using=self._db)
    #
    #     return user


class AbstractModel(models.Model):
    public_id = models.UUIDField(
        db_index=True,
        unique=True,
        default=uuid.uuid4,
        editable=False,
    )
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = AbstractManager()

    class Meta:
        abstract = True
