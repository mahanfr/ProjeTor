from django.contrib import admin
from .models import Company, Team, Position, JoinRequest
# Register your models here.
admin.site.register(Company)
admin.site.register(Team)
admin.site.register(Position)
admin.site.register(JoinRequest)
