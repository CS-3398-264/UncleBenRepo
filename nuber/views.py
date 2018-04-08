from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Driver, User
from .Serializers import  DriverSerializer, UserSerializer

# list all drivers or makes one


class DriverList(APIView):
    def get(self, request):
        driver = Driver.objects.all()
        driver_serializer = DriverSerializer(driver, many=True)
        return Response(driver_serializer.data)

    def post(self):
        pass


class UserList(APIView):
    def get(self, request):
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return Response(user_serializer.data)

    def post(self):
        pass










