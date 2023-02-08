from rest_framework import serializers

from apps.event.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=(
            'id','date','image','name','location',
        )
        read_only_fields=(
            'company',
        )