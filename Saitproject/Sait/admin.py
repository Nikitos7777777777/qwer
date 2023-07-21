from django.contrib import admin
from .models import *

 
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display=('id','marka','cost')

class OpisanieAdmin(admin.ModelAdmin):
    list_display=('id','hourspower','massa','spudi')

class ModelcarAdmin(admin.ModelAdmin):
    list_display=('id','modele','color')

class ComplectacionAdmin(admin.ModelAdmin):
    list_display=('id','solon','body')

class EnigeAdmin(admin.ModelAdmin):
    list_display=('id','volum','cylinders')


admin.site.register(car,PersonAdmin)

admin.site.register(Opisanie,OpisanieAdmin)

admin.site.register(Modelcar,ModelcarAdmin)

admin.site.register(Complectacion,ComplectacionAdmin)

admin.site.register(Enige,EnigeAdmin)

