from rest_framework import serializers

from .models import UserWeight


class PostUserWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWeight
        fields = ["user_id", "day", "weight"]


class GetUserWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWeight
        fields = ["day", "weight"]
