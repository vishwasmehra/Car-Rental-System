from django.db import models

# Create your models here.
#First table for regsitration of a new user
class Register(models.Model):
    first_name =models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    new_password=models.CharField(max_length=300)
    confirm_password=models.CharField(max_length=300)
    birthday=models.CharField(max_length=150)
    gender=models.CharField(max_length=100)

class Profile(models.Model):
    reg= models.ForeignKey(Register, on_delete=models.CASCADE)



