from django.db import models

# Create your models here.
class CityField(models.CharField):
    def to_python(self, value):
        return value.capitalize()

class City(models.Model):
    name = CityField(max_length = 25,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

class Feedback(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    phone = models.CharField(max_length = 13 )
    message = models.TextField()

    def __str__(self):
        return self.first_name
