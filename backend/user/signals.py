from django.db.models.signals import post_save, post_delete, pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from user.models import Profile
import os
User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_delete, sender=Profile)
def auto_delete_profile_pic_on_delete(sender, instance, **kwargs):
    if instance.profile_picture:
        if os.path.isfile(instance.profile_picture.path) and not 'default.jpg' in str(instance.profile_picture.path):
            os.remove(instance.profile_picture.path)

# AUTO DELETE PROFILE PICS AFTER MODEL MODIFIED


@receiver(pre_save, sender=Profile)
def auto_delete_profile_pic_on_change(sender, instance, **kwargs):
    if not instance.id:
        return False

    try:
        old_file = Profile.objects.get(id=instance.id).profile_picture
    except Profile.DoesNotExist:
        return False

    new_file = instance.profile_picture
    if old_file and not old_file == new_file and not 'default.png' in str(old_file.path):
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
