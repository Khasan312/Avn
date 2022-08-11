from rest_framework.urls import path
from .payment import PAYMENT_URL
from .views import *


urlpatterns = [
    path(PAYMENT_URL, PaymentView.as_view()),
]