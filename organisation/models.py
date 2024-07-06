import uuid
from django.db import models
from user.models import User


class Organisation(models.Model):
    """
    Model representing an organisation
    """
    orgId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    users = models.ManyToManyField(User, related_name='organisations')

    def __str__(self):
        return self.name
