from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_purchaser = models.BooleanField(default=False, verbose_name='Kupujący')

    def __str__(self):
        return '{0} - {1}'.format(self.user.username, self.is_purchaser)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)

