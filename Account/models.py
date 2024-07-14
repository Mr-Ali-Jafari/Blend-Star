from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)

    picture = models.ImageField(upload_to="profile/pictures/",blank=True)
    desc = models.TextField()
    birthday = models.DateField()
    gender = models.CharField(max_length=6,choices=[("female","female"),("male","male")])
    universe = models.CharField(max_length=80)

