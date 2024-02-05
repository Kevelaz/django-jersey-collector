from django.db import models

# Create your models here.
class Jersey(models.Model):
  name = models.CharField(max_length=50)
  name_of_sport = models.CharField(max_length=25)
  jersey_number = models.IntegerField()

  def __str__(self):
    return self.name