from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    ordering = ('-date_joined',)
    list_display = ('username','role','is_active')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(User,CustomUserAdmin)
