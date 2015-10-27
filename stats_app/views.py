from rest_framework import viewsets
from .models import Activity, Stat
from .serializers import ActivitySerializer, StatSerializer

# Create your views here.


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer
