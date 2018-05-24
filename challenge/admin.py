from django.contrib import admin

from .models import ChallengeTypes
from .models import Challenge

# Register your models here.
admin.site.register(ChallengeTypes)
admin.site.register(Challenge)