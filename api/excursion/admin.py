from django.contrib import admin

from django.contrib import admin

from . import models


class ExcursionAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "user")


admin.site.register(models.Excursion, ExcursionAdmin)
