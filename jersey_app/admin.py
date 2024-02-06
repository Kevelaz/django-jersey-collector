from django.contrib import admin
# import your models here
from .models import Jersey, Team, Club

# Register your models here
admin.site.register(Jersey)

admin.site.register(Team)

admin.site.register(Club)