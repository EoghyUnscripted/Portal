from django.contrib import admin

from .models import ToDoList

# Combine Models
mods = (ToDoList)

# Register Models
admin.site.register(mods)