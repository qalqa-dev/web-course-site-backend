from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    exclude = ("img",)


admin.site.register(Person, PersonAdmin)
