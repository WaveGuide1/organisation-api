from django.db import models
import uuid


# Create your models here.

class Organisation(models.Model):
    orgId = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField(max_length=500, null=False, blank=False)
    description = models.CharField()

    def __str__(self):
        return self.name
