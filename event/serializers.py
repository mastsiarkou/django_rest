from . models import Timer
from rest_framework import serializers

class TimerSerializer(serializers.ModelSerializer):
    datetime = serializers.DateTimeField()
    class Meta:
        model = Timer
        fields = ('datetime',)