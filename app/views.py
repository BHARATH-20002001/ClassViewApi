from django.shortcuts import render

# Create your views here.
from app.models import *
from rest_framework.response import Response
from rest_framework.decorators import APIView
from app.serializers import *


class ProducCrud(APIView):
    def get(self,request):
        POD = Product.objects.all()
        PJO = ProdectModSerializers(POD,many=True)
        return Response(PJO.data)
    
    def post(self,request):
        PJDO = request.data
        PDO = ProdectModSerializers(data=PJDO)
        if PDO.is_valid():
            PDO.save()
            return Response({"Data":"data inserted successfully"})
        else:
            return Response({"Error":"data is not inserted"})
    