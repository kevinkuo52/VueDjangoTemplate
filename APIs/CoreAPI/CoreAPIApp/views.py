from rest_framework import viewsets
from . import models
from . import serializers

class PaperViewset(viewsets.ModelViewSet):
    queryset = models.Paper.objects.all()
    serializer_class = serializers.PaperSerializer