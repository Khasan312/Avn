import random 
import string


#FOR TXN_ID
def random_string_generator(size=20, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_txn_id_order(instance):
    new_txn_id = random_string_generator()
    Payment = instance.__class__
    py_exists = Payment.objects.filter(txn_id=new_txn_id).exists()
    if py_exists:
        return new_txn_id
    return new_txn_id