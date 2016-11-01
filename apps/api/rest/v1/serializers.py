from rest_framework import serializers

from timelines.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'text', 'user', 'created')
