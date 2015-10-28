from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from .models import Activity, Stat
from .serializers import ActivitySerializer, StatSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import detail_route, api_view

from .permissions import IsUser
from rest_framework.response import Response

# Create your views here.

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    permission_classes = (IsUser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StatViewSet(viewsets.ModelViewSet):
    queryset = Stat.objects.all()
    serializer_class = StatSerializer

    permission_classes = (IsUser)

    def get_quesyset(self):
        activity_pk = self.kwargs['activity_pk']
        get_object_or_404(Activity, pk=activity_pk)
        return self.queryset.filter(activity_id=activity_pk)

    def get_serializer_context(self):
        context = super().get_serializer_context().copy()
        context['activity_pk'] = self.kwargs['activity__pk']
        return context
        # return {'activity_pk': self.kwargs['activity_id']}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


@api_view(['GET'])
def whoami(request):
    user = request.user
    if user.is_authenticated():
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response('', status=status.HTTP_404_NOT_FOUND)
