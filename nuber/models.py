from django.db import models


class Driver(models.Model):
    driver_name = models.CharField(max_length=250)
    driver_status = models.CharField(max_length=20)
    driver_long = models.FloatField(max_length=50)
    driver_lat = models.FloatField(max_length=50)


    def __str__(self):
        return self.driver_name + ' - ' + self.driver_status


class User(models.Model):
    user_name = models.CharField(max_length=250)
    user_long = models.FloatField(max_length=50)
    user_lat = models.FloatField(max_length=50)
    user_status = models.CharField(max_length=20)

    def __str__(self):
        return self.driver_name + ' - ' + self.driver_status

