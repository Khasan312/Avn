from django.db import models
from django.db.models.signals import pre_save
from .utils import  unique_txn_id_order
from django.contrib.auth import get_user_model

User = get_user_model()



CHARSET = '1237812769871682798063764837'
LENGTH = 20



class Payment(models.Model):
    login  = models.CharField(max_length=30, blank=True)
    password = models.CharField(max_length=100, blank=True)
    operator = models.CharField(max_length=100)
    txn_id = models.CharField(max_length=LENGTH, null=True, blank=True, unique=True)
    txn_date = models.DateTimeField(auto_now_add=True)
    account = models.CharField(max_length=12)
    payer_name = models.CharField(max_length=100)
    sum = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    exist = models.BooleanField(default=True)


    def __str__(self) -> str:
        return f'txn_id: {self.txn_id}' 



#GENERATE TXN_ID
def pre_save_create_txn_id(sender, instance, *args, **kwargs):
    if not instance.txn_id:
        instance.txn_id = unique_txn_id_order(instance)

pre_save.connect(pre_save_create_txn_id, sender=Payment)



class CancelPayment(models.Model):
    product = models.ForeignKey(Payment, on_delete=models.CASCADE)
    exist = models.BooleanField(default=True)
    

    
    def __str__(self) -> str:
        return str(self.exist)