from django.contrib import admin
from .models import PriceCard, PriceTable

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'pt_title', 'pt_old_price', 'pt_price')
    list_display_links = ('pt_title', )
    list_editable = ('pt_old_price', 'pt_price')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'pc_value', 'pc_description')
    # list_display_links = ('pt_title', )
    list_editable = ('pc_value', 'pc_description')



admin.site.register(PriceCard, PriceAdmin)
admin.site.register(PriceTable, ServiceAdmin)
