from django.db import models
from datetime import datetime
from users.models import User
# Create your models here.


class Bus(models.Model):

    route = models.CharField(max_length=200)
    bus_no = models.CharField(max_length=200)
    bus_serial_no = models.CharField(max_length=200)
    driver_name = models.CharField(max_length=200)
    starting_point = models.CharField(max_length=200)
    stoppage = models.CharField(max_length=600)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bus_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    add_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.route


class Pass(models.Model):
    route = models.ForeignKey(Bus, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pass_generation_date = models.DateTimeField(
        default=datetime.now, blank=True)

    def __str__(self):
        return self.route.route + " by " + self.user.email
