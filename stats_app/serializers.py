from rest_framework import serializers
from .models import Activity, Stat
from django.contrib.auth.models import User


class StatSerializer(serializers.HyperlinkedModelSerializer):
    activity_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True, source='activity')

    class Meta:
        model = Stat
        fields = ('id', 'count', 'date_done', 'activity_id')

    def create(self, validated_data):
        validated_data['activity_id'] = self.context['activity_pk']
        stat = Stat.objects.create(**validated_data)
        return stat


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    stats = StatSerializer(many=True, read_only=True, required=False)
    act_user = serializers.StringRelatedField(read_only=True, source='user')

    class Meta:
        model = Activity
        fields = ('id', 'act_user', 'act_title', 'act_description', 'created_on', 'stats')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True, source='activity')

    class Meta:
        model = User
        fields = ('username', 'password', 'activities')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
