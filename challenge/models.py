from django.db import models


class ChallengeTypes(models.Model):
    name = models.CharField(max_length=8)
    description = models.TextField()


# Create your models here.
class Challenge(models.Model):
    name = models.CharField(max_length=0x20, null=False)
    description = models.TextField()
    visited_times = models.PositiveIntegerField(null=False, default=0)
    solved_times = models.PositiveIntegerField(null=False, default=0)
    challenge_type = models.ForeignKey(ChallengeTypes, on_delete=models.CASCADE)
    points = models.IntegerField(default=1000)


class Reference(models.Model):
    url = models.URLField()
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)


class Attachment(models.Model):
    url = models.URLField()
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
