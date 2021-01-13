from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="picture")
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Blog(models.Model):
    day = models.IntegerField()
    month = models.TextField()
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to="picture")

class newsblog(models.Model):
    day = models.IntegerField()
    month = models.TextField()
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to="picture")







