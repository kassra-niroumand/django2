from .models import Lead
from rest_framework import viewsets,permissions
from .serializers import LeadSerializer

#LeadViewSet
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permissions_classes  = [
        permissions.AllowAny
    ]2
    serializer_class = LeadSerializer