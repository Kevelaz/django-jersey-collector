from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Club(models.Model):
  name = models.CharField(max_length=50, default = '')
  year_founded = models.IntegerField()
  country_of_origin = models.CharField()
  league_name = models.CharField()

  def __str__(self):
    return self.name



class Jersey(models.Model):
  name = models.CharField(max_length=50)
  name_of_sport = models.CharField(max_length=25)
  jersey_number = models.IntegerField()
  clubs = models.ManyToManyField(Club) 
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class Team(models.Model):
  name = models.CharField(max_length=30, default = '')
  colorway = models.CharField(max_length=30)
  years_on_team = models.IntegerField()
  is_active = models.BooleanField(default = False)

  jersey = models.ForeignKey(Jersey, on_delete = models.CASCADE)

  def __str__(self):
    return f"{self.name}"

