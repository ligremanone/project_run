from app_athletes.models import AthleteInfo
from app_challenges.models import Challenge
from app_positions.models import Position
from django.contrib import admin

from app_run.models import Run

admin.site.register(Run)
admin.site.register(AthleteInfo)
admin.site.register(Challenge)
admin.site.register(Position)
