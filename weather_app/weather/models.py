from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length = 25)

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
