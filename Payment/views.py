from .models import CancelPayment, Payment
from .payment import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CancelSerializer, PaymentAllSerializer, PaymentSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action





class PaymentAllView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentAllSerializer
    

class PaymentView(APIView):
    def post(self, request):
        data = request.data
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            make_payment('login', 'password', 'operator', 'txn_id', 'txn_date', 'account', 'payer_name', 'amount')
            serializer.save()
        return Response({'success': 'Successfully saved'}, status=status.HTTP_200_OK)


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = CancelSerializer
    #####DOEsN'T WORK####
    @action(detail=True, methods=['GET'])
    def cancel_payment(self, request, pk):
        exist = self.get_object()
        pay_obj, created = CancelPayment.objects.get_or_create(exist=exist)
        if pay_obj.exist == True:
            pay_obj.save()
            return Response('added to favorite')
        else:
            pay_obj.exist = not pay_obj.exist
            pay_obj.save()
            return Response('removed from favorite')

    




   