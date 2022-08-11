import requests
import xmltodict

PAYMENT_URL = "https://portal1.avn.kg/paymenttest/api/online-payment/KyrgyzPochta"

def pre_payment_data(login, password, operator, txn_id, txn_date, account, payer_name, amount):
    return f"""<?xml version='1.0' encoding='UTF-8' ?>
<payment>
    <login>{login}</login>
    <password>{password}</password>
    <operator>{operator}</operator>
    <txn_id>{txn_id}</txn_id>
    <txn_date>{txn_date}</txn_date>
    <account>{account}</account>
    <payer_name>{payer_name}</payer_name>
    <sum>{amount}</sum>
</payment>""".encode(
        "utf-8"
    )


def make_payment(login, password, operator, txn_id, txn_date, account, payer_name, amount):
    headers = {"Content-Type": "application/xml; charset=utf-8"}

    data = pre_payment_data(login, password, operator, txn_id, txn_date, account, payer_name, amount)




    response = requests.post(PAYMENT_URL, data=data, headers=headers)
    response_content = xmltodict.parse(response.content)



    return response_content

# make_payment("KyrgyzPochta", "123", "Khasan", "10011001111029", "20160101153100", "201010378101", "Плательщик", "2.00")

payment = make_payment("KyrgyzPochta", "123", "Khasan", "10011000111029", "20160101153100", "201010378101", "Плательщик", "2.00")

print(payment)