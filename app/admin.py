from django.contrib import admin
from .models import Actor

class ActorAdmin(admin.ModelAdmin):
	pass

admin.site.register(Actor, ActorAdmin)

