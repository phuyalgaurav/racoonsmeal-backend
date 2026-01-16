from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(default="Newbiew here", blank=False)
    age = models.IntegerField(blank=False, null=False)
    gender = models.CharField(
        max_length=10,
        choices=[("male", "Male"), ("female", "Female")],
        blank=False,
        null=False,
    )
    profile_picture = models.ImageField(
        upload_to="media/profile_pics/", blank=True, null=True
    )
    height_cm = models.FloatField(blank=False, null=False)
    weight_kg = models.FloatField(blank=False, null=False)
    activity_level = models.CharField(
        max_length=50,
        choices=[
            ("sedentary", "Sedentary"),
            ("light", "Light"),
            ("moderate", "Moderate"),
            ("active", "Active"),
            ("very_active", "Very Active"),
        ],
        null=False,
        default="lightly",
    )
    followers = models.ManyToManyField(User, related_name="following", blank=True)
    goal = models.CharField(
        max_length=50,
        choices=[
            ("cut", "Cut"),
            ("maintain", "Maintain"),
            ("gain", "Gain"),
        ],
        null=False,
        default="maintain",
    )

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.user.username
