from django.db.models.signals import post_save
from job_portal_auth.models import User
from django.dispatch import receiver
from .models import UserProfileModel


@receiver(post_save, sender=User)
def user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfileModel.objects.create(
            user=instance, email=instance.email, phone=instance.phone_number, username=instance.username)
        print("model created")
