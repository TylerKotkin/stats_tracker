from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import Activity, Stat
from .serializers import ActivitySerializer, StatSerializer, UserSerializer
from django.contrib.auth.models import User

# Create your views here.

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

    def get_quesyset(self):
        activity_pk = self.kwargs['activity_pk']
        get_object_or_404(Activity, pk=activity_pk)
        return self.queryset.filter(activity_id=activity_pk)

    def get_serializer_context(self):
        context = super().get_serializer_context().copy()
        context['activity_pk'] = self.kwargs['activity__pk']
        return context
        # return {'activity_pk': self.kwargs['activity_id']}


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
