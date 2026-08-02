from django.db import models

# Create your models here.
class user_register(models.Model):
    username=models.CharField(max_length=100)
    useremail=models.CharField(max_length=100)
    userpassword=models.CharField(max_length=100)
    userphone=models.CharField(max_length=100)
    usercity=models.CharField(max_length=100)

class booking_app(models.Model):
     user_name=models.CharField(max_length=100)
     user_email=models.EmailField()
     user_phone=models.CharField(max_length=15)
     user_destination=models.CharField(max_length=100)
     status=models.CharField( max_length=20,default='Pending')


class contact_us_details(models.Model):
     username_c=models.CharField(max_length=100)
     useremail_c=models.CharField(max_length=100)
     userphone_c=models.CharField(max_length=100)
     message_c=models.CharField(max_length=100)
  

