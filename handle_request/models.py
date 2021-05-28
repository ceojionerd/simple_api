from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.utils import timezone
import uuid



def unique_uuid():
    while True:
        uidd = uuid.uuid4().hex
        if not UUID.objects.filter(uuid=uidd).exists():
            return uidd

class UUID(models.Model):
    STATUS_CHOICES = [
        ('Cr', 'Created'),
        ('Pn', 'Pending')
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    uuid = models.CharField(max_length=35, default=unique_uuid)

    def __str__(self):
        return self.uuid
