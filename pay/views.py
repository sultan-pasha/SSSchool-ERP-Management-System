from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json
# Create your views here.


def paykey(tok, price):
	url = 'https://accept.paymob.com/api/acceptance/payment_keys'
	data = {
    "auth_token": tok,
    "amount_cents":price,
    "expiration": 3600,
    "order_id":"57746180",
    "billing_data":{
                    "apartment": "NA", 
                    "email": "claudette09@exa.com", 
                    "floor": "NA", 
                    "first_name": "Clifford", 
                    "street": "NA", 
                    "building": "NA", 
                    "phone_number": "+86(8)9135210487", 
                    "shipping_method": "NA", 
                    "postal_code": "NA", 
                    "city": "NA", 
                    "country": "NA", 
                    "last_name": "Nicolas", 
                    "state": "NA"
                    },
    "currency":"EGP",
    "integration_id":2388936,
	"lock_order_when_paid":True
}
	response = requests.post(url, json=data)
	jsondata = response.json()
	paytok = jsondata['token']
	return paytok



def orderreg(tok, price):
	url = 'https://accept.paymob.com/api/ecommerce/orders'
	data = {
	"auth_token": tok,
	"delivery_needed": False,
    "amount_Cents":True,
    "amount_cents":price,
    "items":[]  
}
	response = requests.post(url, json=data)
	jsondata = response.json()
	ordertoken = jsondata['token']


def token(request):
	if request.method == 'POST':
		url = 'https://accept.paymob.com/api/auth/tokens'
		data = {"api_key": "ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmpiR0Z6Y3lJNklrMWxjbU5vWVc1MElpd2ljSEp2Wm1sc1pWOXdheUk2TWpRd01qRTJMQ0p1WVcxbElqb2lhVzVwZEdsaGJDSjkuRVl0bExWdzVKMHJVZmJqbElXb3Y1Nk4zd29ZcXB3SUNSNWptMjQ3bTczREhKRXgxQUxRU3J5RmRBeTNtZEhjZFNJV0FkRjh4amJfZ1N2bFNpX2lPR0E="}
		response = requests.post(url, json=data)
		jsondata = response.json()
		tokenauth = jsondata['token']
		price = str(int(request.POST['amount']) * 100)
		orderreg(tokenauth, price)
		return redirect('https://accept.paymobsolutions.com/api/acceptance/iframes/%s?payment_token=%s' %(429186, paykey(tokenauth, price)))
	else:
		return render(request, 'pay.html')