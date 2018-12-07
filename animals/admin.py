from django.contrib import admin
from .models import UserVet, UserProfile, Vaccine, Antiparasitic, Animal, ClinicalRecord, Inmunization, Deworming, UserVet
# Register your models here.

class ClinicalRecordInLine(admin.TabularInline):
    model = ClinicalRecord
    extra = 0 #campos para registrar

class UserVetAdmin(admin.ModelAdmin):
    list_display = ('user', 'cedula_profesional', 'clinic_name')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('create_at', 'city', 'colony', 'state', 'country', 'phone')
    
class VaccineAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class AntiparasiticAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'adoption_day', 'species', 'sex','castrating', 'modified_at', 'created_at')
    inlines = (ClinicalRecordInLine,)
class InmunizationAdmin(admin.ModelAdmin):
    list_display = ('vaccine', 'application_date', 'reapplication_date')

class DewormingAdmin(admin.ModelAdmin):
    list_display = ('antiparasitic', 'application_date', 'reapplication_date')

class InmunizationInLine(admin.TabularInline):
    model = Inmunization
    extra = 0

class DewormingInLine(admin.TabularInline):
    model = Deworming
    extra = 0

class ClinicalRecordAdmin(admin.ModelAdmin):
    list_display = ('diagnostic','treatment', 'examination_date')
    inlines = (InmunizationInLine,DewormingInLine)




admin.site.register(UserVet, UserVetAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(Antiparasitic, AntiparasiticAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Inmunization, InmunizationAdmin)
admin.site.register(Deworming, DewormingAdmin)
admin.site.register(ClinicalRecord, ClinicalRecordAdmin)
 #esto importa