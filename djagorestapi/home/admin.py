from django.contrib import admin
from home.models import Person, Team

# Register your models here.

admin.site.register(Team)
admin.site.register(Person)