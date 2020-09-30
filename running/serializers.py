from rest_framework import serializers
from .models import Running
from .models import Users


class RunningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Running
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    running = RunningSerializer(many=True)

    class Meta:
        model = Users
        fields = '__all__'
