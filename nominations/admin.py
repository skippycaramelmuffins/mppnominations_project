from django.contrib import admin
from .models import Voter, Nomination, Position, Vote

# Register your models here.
admin.site.register(Voter)
admin.site.register(Nomination)
admin.site.register(Position)
admin.site.register(Vote)
