import time

from .serializers import ItemSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from cloudipsp import Api, Checkout


class ItemsPage(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class OrderAdd(APIView):
    def post(self, req):
        order = OrderSerializer(data=req.data)
        if order.is_valid():
            order.save()
            api = Api(merchant_id=1396424,
                      secret_key='test')
            checkout = Checkout(api=api)
            data = {
                "currency": "USD",
                "amount": int(req.data['suma']) * 100,
                "order_desc": "Platność za towar",
                "order_id": str(time.time())
            }
            url = checkout.url(data).get('checkout_url')

            return Response({'result': 'Jeszcze chwilkę...', 'url': url})

        return Response({'result': 'Bląd w formie'})
