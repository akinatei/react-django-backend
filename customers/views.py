from django.http import request, JsonResponse
from customers.models import Customer
from customers.serializers import CustomerSerializer
def customers(request):
    #invoke serializer and return to client
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers': serializer.data})