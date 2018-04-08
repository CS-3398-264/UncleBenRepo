from rest_framework import serializers
from .models import Driver, User


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'