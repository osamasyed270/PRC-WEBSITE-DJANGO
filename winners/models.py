from django.db import models
from django.utils.timezone import now

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_products(self):
         return Winner.objects.filter(categories__name=self.name)

class Winner(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    sno = models.AutoField(primary_key=True)
    categories = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=1000, blank=True)
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices = GENDER_CHOICES, default="male")
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.full_name
        
class Match_1_Winner(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    sno = models.AutoField(primary_key=True)
    image_url = models.CharField(max_length=1000, blank=True)
    full_name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=100, choices = GENDER_CHOICES, default="male")
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.full_name

