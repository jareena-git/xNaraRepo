from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from .models import CustomerData
from .serializers import CustomerDataSerializer
import uuid

# Create your views here.
def customer_data_view(request):
    '''This view take request as input, we are going to call two different apis and generating json and displaying on UI'''

    if request.method == "GET":
        try:
            pack1 = requests.\
                get("https://6466e9a7ba7110b663ab51f2.mockapi.io/api/v1/pack1").json()
            pack2 = requests.\
                get("https://6466e9a7ba7110b663ab51f2.mockapi.io/api/v1/pack2").json()

            customer_data = []
            for data in pack1:
                customer_data.\
                    append({'customer_id':data['customer_id'],"pack1":data['pack_data']})

            for data in pack2:
                customer_data.\
                    append({'customer_id':data['customer_id'],"pack2":data['pack_data']})

            # customer_data_obj = CustomerData.objects.\
            #     create(customer_id=data['customer_id'],customer_data=customer_data)
            #
            # serializer = CustomerDataSerializer(customer_data_obj)

            return JsonResponse(customer_data,\
                                status=status.HTTP_201_CREATED,safe=False)

        except Exception as e:
            return JsonResponse({'error':'An error occurred while calling API',\
                                 status:status.HTTP_500_INTERNAL_SERVER_ERROR},safe=False)

