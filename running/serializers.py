from rest_framework import serializers
from .models import Running, Users



class RunningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Running
        fields = ("id", "name", "picture_url","party_affiliation", "campaign_website", "social", "quote", "position" )


class UsersSerializer(serializers.ModelSerializer):
    running = RunningSerializer(read_only=True, many=True)

    class Meta:
        model = Users
        fields = ("id", "name", "email", "address", 'running' )
