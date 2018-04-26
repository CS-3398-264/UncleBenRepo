from rest_framework import routers, serializers, viewsets
from users.models import Driver


class DriverSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(source='user.first_name')

	class Meta:
		model = Driver
		fields = ('first_name', 'phone')