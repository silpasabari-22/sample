from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
# class custom_user(AbstractUser):
#     age=models.IntegerField()
#     phno=models.IntegerField(max_length=10)



class profile(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    phno=models.IntegerField()


