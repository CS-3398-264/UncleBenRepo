from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework import routers, serializers, viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from cabs.serializers import CabSerializer
from cabs.models import Cab


class CabViewSet(viewsets.ModelViewSet):
    queryset = Cab.objects.all()
    serializer_class = CabSerializer


class NearBy(APIView):

    def post(self, request, format=None):
    	try:
    		latitude = request.data['latitude']
    	except KeyError:
    		raise exceptions.ValidationError("Please enter a valid latitude")

    	try:
    		longitude = request.data['longitude']
    	except KeyError:
    		raise exceptions.ValidationError("Please enter a valid longitude")
    	
    	location = Point(float(longitude), float(latitude), srid=4326)
    	cabs = Cab.objects.all().annotate(distance=Distance('current_location', location)).order_by('distance')[0:5]
        serializer = CabSerializer(cabs, many=True)
        return Response(serializer.data)