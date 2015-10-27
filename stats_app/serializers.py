from rest_framework import serializers
from .models import Activity, Stat


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
    # stats = StatSerializer(many=True)

    class Meta:
        model = Activity
        fields = ('id', 'user_id', 'act_title', 'act_description', 'created_on')
