from django.contrib import admin
from .models import UserVet

# Register your models here.
class UserVetAdmin(admin.ModelAdmin):
    list_display = ('user', 'cedula_profesional', 'clinic_name')

admin.site.register(UserVet) #esto importa