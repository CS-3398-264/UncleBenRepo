# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class Driver(models.Model):
    user = models.OneToOneField(User)
    ssn = models.CharField(max_length=100)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=12, null=True)

    def __str__(self):
        return self.user.email

