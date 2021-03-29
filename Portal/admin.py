from django.contrib import admin

from .models import Demo

# Combine Imported Models
mods = (Demo)

# Register Models
admin.site.register(mods)
