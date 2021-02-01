from django.contrib import admin

from .models import Percentage

# Combine Models
mods = (Percentage)

# Register Models
admin.site.register(mods)