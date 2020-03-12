from django.contrib.auth.models import User, Group
from . import models
from rest_framework import serializers


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Paper
        fields = ('id', 'title', 'abstract')
