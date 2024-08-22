from rest_framework import viewsets
from .models import Royxat
from .serializers import RoyxatSerializer

class RoyxatViewSet(viewsets.ModelViewSet):
    queryset = Royxat.objects.all()
    serializer_class = RoyxatSerializer
