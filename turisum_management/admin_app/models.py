from django.db import models

# Create your models here.
class Package_details(models.Model):
    image=models.ImageField(default="")
    packagename=models.CharField(max_length=100)
    package=models.IntegerField(default=0)
    location=models.CharField(max_length=100)
    days=models.CharField(max_length=100)


class hotel_adbooking_details(models.Model):
    username_hb=models.CharField(default="")
    useremail_hb=models.CharField(default="")
    userphone_hb=models.CharField(default="")
    hotel_name=models.CharField(default="")
    check_in=models.DateField(default="")
    check_out=models.DateField(default="")
    guest=models.CharField(default="")
    vehicle_hb=models.CharField(default="")
    destination=models.CharField(default="")