from django.contrib import admin

# Register your models here.

from .models import Case,User,Area,CaseState

class UserAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Case)
admin.site.register(User,UserAdmin)
admin.site.register(Area)
admin.site.register(CaseState)