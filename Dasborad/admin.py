from django.contrib import admin
from .models import product, order
#from django.contrib.auth.models import Group
admin.site.site_header = 'NATERs Dashboard'

class productadmin (admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']


admin.site.register(product,productadmin)
admin.site.register( order)
# admin.site.unregister(Group)
