from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import User, UserProfile
from .models import UserRequirementStat
from .util import compute_nutrition_for_user


# Make usernutrients when a userprofile is created
@receiver(post_save, sender=UserProfile)
def create_user_nutrient_requirements(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.get(pk=instance.pk)
        user_data = {
            "height_cm": user_profile.height_cm,
            "weight_kg": user_profile.weight_kg,
            "age": user_profile.age,
            "gender": user_profile.gender,
            "activity_level": user_profile.activity_level,
            "goal": user_profile.goal,
        }
        nutrition_info = compute_nutrition_for_user(user_data)
        UserRequirementStat.objects.create(user=instance.user, **nutrition_info)
