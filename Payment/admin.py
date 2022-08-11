from django.contrib import admin
from .models import CancelPayment, Payment



class PaymentAdmin(admin.ModelAdmin):
    list_display = ('txn_id',) 

admin.site.register(Payment, PaymentAdmin)
admin.site.register(CancelPayment)