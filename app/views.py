from django.shortcuts import render

# Create your views here.
from app.models import *
from rest_framework.response import Response
from rest_framework.decorators import APIView
from app.serializers import *


class ProducCrud(APIView):
    def get(self,request,prod_id):
        #POD = Product.objects.all()
        #PJO = ProdectModSerializers(POD,many=True)#give many=true for get all 

        POD = Product.objects.get(prod_id=prod_id)
        PJO = ProdectModSerializers(POD)
        return Response(PJO.data)


    def post(self,request):
        PJDO = request.data
        PDO = ProdectModSerializers(data=PJDO)
        if PDO.is_valid():
            PDO.save()
            return Response({"Data":"data inserted successfully"})
        else:
            return Response({"Error":"data is not inserted"})


    def put(self,request,prod_id):
        PO = Product.objects.get(prod_id=prod_id)
        PDO = ProdectModSerializers(PO,data=request.data)
        if PDO.is_valid():
            PDO.save()
            return Response({"updated":"data inserted successfully"})
        else:
            return Response({"Error":"data not updated"})
        
    def patch(self,request,prod_id):
        PO=Product.objects.get(prod_id=prod_id)
        UPDO=ProdectModSerializers(PO,data=request.data,partial=True)
        if UPDO.is_valid():
            UPDO.save()
            return Response({'update':'Data is Updated'})
        else:
            return Response({'error':'Update not done'})
        
    def delete(self,request,prod_id):
        Product.objects.get(prod_id=prod_id).delete()
        return Response({'deletion':'Data is Deleted'})