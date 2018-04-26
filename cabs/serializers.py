from rest_framework import routers, serializers, viewsets
from cabs.utils import PointField
from cabs.models import Cab
from users.serializers import DriverSerializer


class CabSerializer(serializers.ModelSerializer):
    current_location = PointField()
    driver = DriverSerializer(read_only=True)

    class Meta:
        model = Cab
        fields = ('pk', 'vin_number', 'model', 'status', 'current_location', 'driver')