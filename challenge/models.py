from django.db import models

class ChallengeTypes(models.Model):
    name = models.CharField(max_length=8)
    description = models.TextField()

# Create your models here.
class Challenge(models.Model):
    name = models.CharField(max_length=0x20, null=False)
    description = models.TextField()
    # references
    # attachments
    visited_times = models.PositiveIntegerField(null=False, default=0)
    sovled_times = models.PositiveIntegerField(null=False, default=0)
    # rank
    challenge_type = models.ForeignKey(ChallengeTypes, on_delete=models.CASCADE)
    points = models.IntegerField(default=1000)
