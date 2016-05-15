from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserRecipeSuggestions(models.Model):
    created_by = models.BigIntegerField()
    email = models.EmailField(max_length=75)
    apk_version = models.IntegerField(null=True, blank=True)
    subscription_type = models.IntegerField(null=True)
    suggested_food = models.CharField(max_length=200)
    problem = models.IntegerField(default=0)
    same_as = models.CharField(max_length=50)
    action_taken = models.CharField(max_length=200)
    gcm_push = models.BooleanField(default=False)
    email_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.email

