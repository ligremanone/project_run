from django.contrib import admin

from app_run.models import Run
from app_positions.models import Position
from app_challenges.models import Challenge
from app_athletes.models import AthleteInfo

admin.site.register(Run)
admin.site.register(AthleteInfo)
admin.site.register(Challenge)
admin.site.register(Position)
