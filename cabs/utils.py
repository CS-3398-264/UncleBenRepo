import re
from rest_framework import serializers


class PointField(serializers.Field):

    valid_data_re = re.compile(r"-?[0-9]+\.?[0-9]+, *-?[0-9]+\.?[0-9]+")
    default_error_messages = {
        "invalid_input": "Need two values representing lat and lng separated by comma. ex: 1.234, 25.2345"
    }

    def to_representation(self, value):
        return value.tuple

    def to_internal_value(self, data):
        if not self.valid_data_re.match(data):
            self.fail("invalid_input")
        data = [float(item.strip()) for item in data.split(",")]
        return Point(*data, srid=4326)