# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models
from users.models import Driver


STATUS = (
    ('available', 'Available'),
    ('occupied', 'Occupied'),
    ('offline', 'Offline'),
)

class Cab(models.Model):
	vin_number = models.CharField(max_length=20)
	current_location = models.PointField()
	model = models.CharField(max_length=200)
	status = models.CharField(choices=STATUS, max_length=100)
	driver = models.ForeignKey(Driver, null=True)

	def __str__(self):
		return self.vin_number
