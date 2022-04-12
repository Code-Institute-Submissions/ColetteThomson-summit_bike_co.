from django.db import models
from django.contrib.auth.models import User
# post_save and receiver needed for signal to work
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """ user profile model for maintaining default
    delivery information and order history """
    # each user has one profile and each profile has one user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # default and optional delivery information fields (from Order model)
    default_phone_number = models.CharField(max_length=20, null=True,
                                            blank=True)
    default_country = CountryField(blank_label='Country *', null=True,
                                   blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True,
                                            blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True,
                                               blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    # string method to return user name
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ each time a user object is saved, either create a profile for them if
    a new user, or save the profile to update it if user already exists."""
    if created:
        UserProfile.objects.create(user=instance)
    # existing users: just save the profile
    instance.userprofile.save()
