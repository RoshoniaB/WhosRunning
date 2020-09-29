from rest_framework import serializers
from .models import Running


class RunningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Running
        fields = '__all__'
