from django.contrib import admin

# Models
from .models import Country, Election, ElectoralProfile, MediaOutlet

# Register your models here.
admin.site.register(Country)
admin.site.register(Election)
admin.site.register(ElectoralProfile)
admin.site.register(MediaOutlet)