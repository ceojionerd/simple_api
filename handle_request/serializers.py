from django.db import models
from django.db.models import fields
from rest_framework import serializers
from handle_request.models import UUID

class UUIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = UUID
        fields = ('timestamp', 'uuid')

