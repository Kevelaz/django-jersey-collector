from django.contrib import admin
# import your models here
from .models import Jersey, Team

# Register your models here
admin.site.register(Jersey)

admin.site.register(Team)