from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, IntegerField, CASCADE


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    shoe_size = IntegerField()
# Create your models here.
