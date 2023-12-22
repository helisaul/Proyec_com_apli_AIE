from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Usuario)

admin.site.site_header = 'Mi Panel de Administración'
admin.site.site_title = 'Mi Panel de Administración'
admin.site.index_title = 'Bienvenido a Mi Panel de Administración'

