from django.db import models
from django.utils.timezone import now

# Create your models here.

class Match_1_Register(models.Model):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
    )
    sno = models.AutoField(primary_key=True)
    image = models.URLField()
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile_no = models.CharField(max_length=11)
    name_in_game = models.CharField(max_length=100)
    game_id = models.CharField(max_length=20)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=100, choices = GENDER_CHOICES, default="male")
    facebook_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.full_name + ' ---- ' + self.email + ' ---- ' + self.mobile_no + ' ---- ' + self.game_id