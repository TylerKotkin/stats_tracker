from django.contrib import admin
from .models import Activity, Stat


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'act_title', 'created_on']


class StatAdmin(admin.ModelAdmin):
    list_display = ['id', 'activity_id', 'count', 'date_done']


# Register your models here.

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Stat, StatAdmin)
