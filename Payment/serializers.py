from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework import serializers
from .models import Payment


class PaymentAllSerializer(serializers.ModelSerializer):


    class Meta:
        model = Payment
        fields = '__all__'

        

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    

    class Meta:
        model = Payment
        fields = ['url', 'login', 'password', 'operator', 'txn_id', 'txn_date', 'account', 'payer_name', 'sum']
        

class CancelSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'