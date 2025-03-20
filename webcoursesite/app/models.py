from django.db import models


class Person(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    img = models.ImageField(upload_to="")
