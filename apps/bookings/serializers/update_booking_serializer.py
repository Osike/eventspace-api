from rest_framework import serializers
from ..models import Event

class EventUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'event_name', 
            'start_datetime', 
            'end_datetime', 
            'organizer_name', 
            'organizer_email', 
            'event_type', 
            'attendance'
        ]

    def validate(self, data):
        start_datetime = data.get('start_datetime', self.instance.start_datetime)
        end_datetime = data.get('end_datetime', self.instance.end_datetime)

        if start_datetime and end_datetime:
            if start_datetime >= end_datetime:
                raise serializers.ValidationError("End datetime must be after start datetime")

        return data
