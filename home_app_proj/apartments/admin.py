from django.contrib import admin
from .models import Apart, Owner, Service


# Register your models here.
# admin.site.register(Apart)
# admin.site.register(Owner)


# Define the admin class
class ApartAdmin(admin.ModelAdmin):
    list_display = ('nbr', 'descr', 'owner', 'summary', 'layout') 
    list_filter = ('descr', 'owner')
    fieldsets = (
        (None, {
            'fields': ('nbr','descr','owner')
        }),
        ('Specs', {
            'fields': ('summary', 'layout')
        }),
    )
   


# Register the admin class with the associated model
admin.site.register(Apart, ApartAdmin)


# Register the Admin classes for Owner using the decorator
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone')
    fields = [('last_name', 'first_name'), 'phone']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('prof_req', 'date_req')
    list_filter = ('prof_req', 'date_req')
    fieldsets = (
        (None, {
            'fields': ('prof_req', 'date_req', 'client')
        }),        
    )



