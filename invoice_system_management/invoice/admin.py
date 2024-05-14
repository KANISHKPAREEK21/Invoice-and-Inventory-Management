from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_price',
                    'product_unit', 'product_is_delete']


# this is comment
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name',
                    'customer_amount', 'customer_contact']
# this is comment


class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice', 'product', 'amount']


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'customer', 'total']


# Register your models here.
admin.site.register(Product, ProductAdmin)

# this is comment
admin.site.register(Customer, CustomerAdmin)
# this is comment

admin.site.register(InvoiceDetail, InvoiceDetailAdmin)
admin.site.register(Invoice, InvoiceAdmin)
