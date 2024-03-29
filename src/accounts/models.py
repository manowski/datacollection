import uuid
from django.db import models

from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken


class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Throttling per hour
    tier = models.IntegerField(default=0)

    def get_tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def __str__(self):
        return self.username

