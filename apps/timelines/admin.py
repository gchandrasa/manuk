from django.contrib import admin

from .models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', '__unicode__', 'created')


admin.site.register(Status, StatusAdmin)
