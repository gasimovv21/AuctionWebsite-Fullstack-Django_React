import requests
from django.conf import settings
from rest_framework.response import Response


from django.http import HttpResponse
import json

def getPaypalDataDetail(request):
    paypal_client_id = settings.PAYPAL_CLIENT_ID
    response_data = {
        'paypal_client_id': paypal_client_id
    }
    response_json = json.dumps(response_data)
    response = HttpResponse(response_json, content_type='application/json')
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    response["Access-Control-Allow-Methods"] = "GET"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    return response

